#include "HX711.h"
#include <TimeLib.h>
// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;
HX711 scale;
void scale_setup()
{
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  Serial.println("Before setting up the scale:");
  Serial.print("read: \t\t");
  Serial.println(scale.read());      // print a raw reading from the ADC
  scale.set_scale(775.f);  //940                    // tăng thi gia trị thực giảm
  //scale.set_scale(500.f);  
  scale.tare();               // reset the scale to 0
}

// Test cân 
void test_can()
{
    float lys=0;
    while(true)
    {
      lys = scale.get_units();
      Serial.println(lys);
    }
}


// Khai báo các chân relay
#define RST 12
#define RSD 11
#define RNC 10
#define RND 9
#define RVC 8

//Khởi tạo các chân output cho relay 

void relay_setup()
{
  pinMode(RST, OUTPUT); pinMode(RSD, OUTPUT);  
  pinMode(RNC, OUTPUT); pinMode(RND, OUTPUT);  
  pinMode(RVC, OUTPUT);
  digitalWrite(RST, LOW); digitalWrite(RSD, LOW);  
  digitalWrite(RNC, LOW); digitalWrite(RND, LOW);  
  digitalWrite(RVC, LOW);
}

void vesinh()
{
  digitalWrite(RNC, HIGH); 
  digitalWrite(RST, HIGH); 
  digitalWrite(RND, HIGH);
  digitalWrite(RVC, HIGH);
  digitalWrite(RND, HIGH);
  delay(20000);
    digitalWrite(RNC, HIGH); 
  digitalWrite(RSD, HIGH); 
  digitalWrite(RND, HIGH);
  digitalWrite(RVC, HIGH);
  digitalWrite(RND, HIGH);
}
// Hàm kiểm tra
void test_relay()
{
       //Serial.println("Sua tuoi");
      //digitalWrite(RST, HIGH); delay(2000); digitalWrite(RST, LOW);delay(2000);
      
       //Serial.println("Nuoc cam ");
      //digitalWrite(RNC, HIGH); delay(2000); digitalWrite(RNC, LOW);  
      //delay(2000);
      // Serial.println("Sua dau");
      //digitalWrite(RSD, HIGH); delay(1000); digitalWrite(RSD, LOW);
//delay(1000);
  //     Serial.println("nuoc duong");
   //   digitalWrite(RND, HIGH);  delay(2000); digitalWrite(RND, LOW);
   //   delay(2000);
      // Serial.println("vichat");

     // digitalWrite(RVC, HIGH);  delay(3000); digitalWrite(RVC, LOW);
     // delay(2000);
      //*/
      test_can();
}
// Khai báo biến nhận và thông số dinh dưỡng
char buffer[10];
int index=1;
int ST=100,SD=100,NC=100;
float cup = 150;// một ly 150ml 
bool vichat=0;
int luongnuoc=150;
int tyle=0;

void bom(int type,int input)
{   //Xu Li Data
    luongnuoc=input/100;
    int bientam=input%100;
    tyle=bientam%10;
    vichat=bientam/10;

    Serial.print("Lượng nước: ");Serial.println(luongnuoc);
    Serial.print("Tỷ lệ: ");Serial.println(tyle);
    Serial.print("Vi chất: ");Serial.println(vichat);
    
    // thực hiện kiểm tra đã đặt ly chưa 
    Serial.print("KiemtraLy");
    float ly=0; //khai báo giá trị cân ban đầu
    setTime(0, 0, 0, 0, 0, 0);// đưa thời gian về 0
    int limit=10,count=0;// khai báo thời gian 
    while(true)
    {
      count=second();
      ly = scale.get_units();

      if(ly<=3) {
        //Serial.print("Dem thoi gian : ");
        Serial.println(count);
      }
      else {
        Serial.println("ĐÃ để ly");
        delay(1500);
        break;
      }
      if(count>=limit) {
        Serial.println("nhắc nhở chưa để ly");
        Serial.println("@");      // gui tin hieu den pycharm de nhac nho chua de ly
        setTime(0, 0, 0, 0, 0, 0);// đưa thời gian về 0
        limit=15;
        count=0;// khai báo thời gian      
      }
    }
    // nếu có bơm vi chất thì bơm
    if(vichat==1){
      Serial.println("Bơm vi chất");
      digitalWrite(RVC, HIGH);  delay(100); digitalWrite(RVC, LOW);
    }
     delay(2000);
    // Bơm sữa tươi 
    Serial.println("Bơm nước chính");
    
    Serial.print(type);
    float giatrido=scale.get_units(); 
    float error=0;
    float saiso=3;
    ly=8.8;
    if(type==1) digitalWrite(RST, HIGH);
    else if(type==2) digitalWrite(RSD, HIGH);
    else if(type==3) digitalWrite(RNC, HIGH);
    while(true)
    {
      giatrido=scale.get_units()-ly;
      Serial.println(giatrido);
      error=giatrido-luongnuoc;
      if((abs(error)<=saiso)||(error>=0)) break;
    }
    if(type==1) digitalWrite(RST, LOW);
    else if(type==2) digitalWrite(RSD, LOW);
    else if(type==3) digitalWrite(RNC, LOW);

    // Bơm đường 
    giatrido=scale.get_units(); 
    error=0;
    saiso=3;
    ly=8.8;
    digitalWrite(RND, HIGH);
    float luongduong=tyle*luongnuoc/100;
    while(true)
    {
      giatrido=scale.get_units()-ly;
      //Serial.println(" GIa tri suong ");
      Serial.println(giatrido);
      error=giatrido-(luongnuoc+ luongduong);
      if((abs(error)<=saiso)||(error>=0)) break;
    }
    digitalWrite(RND, LOW);
    Serial.println("&");
    Serial.println("Ket thuc");
}
void setup() {
  // initialize serial:
  Serial.begin(115200);
  scale_setup();
  relay_setup();
  //digitalWrite(RVC, HIGH);  delay(80); digitalWrite(RVC, LOW);
  // delay(2000);

}

void loop() {
  // put your main code here, to run repeatedly:
  //test_relay();
  //vesinh();
  //test_can();
}
void serialEvent() {
  //index=0;
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    buffer[index-1] = inChar;
    //Serial.println(buffer);
    //inputString += inChar;
    if (inChar == '$') {
      //stringComplete = true;
      buffer[index]='\0';
      //Serial.println("hello");
//      for(int i=0;i<=sizeof(buffer);i++)
//        {Serial.print(i);Serial.print(" ");
//        Serial.println(buffer[i]);}
      if (buffer[0] == 'S') {
        ST = strtol(buffer+1, NULL, 10); // Stringto long integer
        Serial.println(ST);
        bom(1,ST);
        //BomCofffee(1,CS,3); 
      }else  if (buffer[0] == 'D') {
        SD = strtol(buffer+1, NULL, 10); // Stringto long integer
        Serial.println(SD);
        bom(2,SD);
      }else  if (buffer[0] == 'C') {
        NC = strtol(buffer+1, NULL, 10); // Stringto long integer
        Serial.println(NC);
        bom(3,NC);
      }
      index=0;
     }
     else index++;
  }
}

