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

float scale_data=0;

#define RCF 11
#define RNC 9
#define RCC 10
#define RS 8
#define RD 12

int type_set=0;
int df=100,dn=150;

String inputString = "";         // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete
char buffer[10];
int index=1;
int CS=90,CD=90,NC=100,CC=100;

void _int_()
{
  pinMode(RCF, OUTPUT); pinMode(RNC, OUTPUT);  
  pinMode(RCC, OUTPUT); pinMode(RS, OUTPUT);  
  pinMode(RD, OUTPUT);
  digitalWrite(RCF, LOW); digitalWrite(RNC, LOW);  
  digitalWrite(RCC, LOW); digitalWrite(RS, LOW);  
  digitalWrite(RD, LOW);
}
void test_relay(int dem)
{
 
      digitalWrite(RCF, HIGH); delay(1000); digitalWrite(RCF, LOW);
      digitalWrite(RNC, HIGH); delay(1000); digitalWrite(RNC, LOW);  
      digitalWrite(RCC, HIGH); delay(1000); digitalWrite(RCC, LOW);
      digitalWrite(RS, HIGH);  delay(1000); digitalWrite(RS, LOW);
      digitalWrite(RD, HIGH);  delay(1000); digitalWrite(RD, LOW);
      delay(1000);
}
void Bomnuoc(int type,int luong, float saiso)
{
    //Bơm nuoc
    int nuoc = luong*dn/100;
    Serial.print("Nuoc: ");
    Serial.println(nuoc);
    float ly=0;
    setTime(0, 0, 0, 0, 0, 0);
    int limit=15,count=0;
    while(true)
    {
      count=second();
      ly = scale.get_units();
      if(ly<=3) Serial.println(count);
      else {
        delay(1500);
        break;
      }
      if(count>=limit) goto ketthuc;
      
    }
    ly = scale.get_units();
    Serial.print("ly: ");
    Serial.println(ly);
    
    if(type==3) digitalWrite(RNC, HIGH);
    else digitalWrite(RCC, HIGH);
    Serial.print(type);
    Serial.println(" gram");
    float giatrido=scale.get_units(); 
    float error=0;
    while(true)
    {
      giatrido=scale.get_units()-ly;
      Serial.print(giatrido);
      Serial.println(" gram cofee ");
      error=giatrido-nuoc;
      if((abs(error)<=saiso)||(error>=0)) break;
    }
    if(type==3) digitalWrite(RNC, LOW);
    else digitalWrite(RCC, LOW);
    ketthuc: 
    if(count<limit)
      Serial.println("Xong Nuoc");
    else Serial.println("Lỗi không ly");
    index=0;
    memset(buffer, 0, sizeof(buffer));

}
void BomCofffee(int type,int luong, float saiso)
{
    //Bơm
    int coffee = luong*df/100;
    Serial.print("coffee: ");
    Serial.println(coffee);
    int sua = df - coffee;
    Serial.print("sữa: ");
    Serial.println(sua);
    
    float ly=0;
    setTime(0, 0, 0, 0, 0, 0);
    int limit=15,count=0;
    while(true)
    {
      count=second();
      ly = scale.get_units();
      if(ly<=3) Serial.println(limit-count);
      else {
        delay(1500);
        Serial.println('$');
        break;
      }
      if(count>=limit) goto ketthuc;
      
    }
    ly = scale.get_units();
    Serial.print("ly: ");
    Serial.println(ly);
    
    if(type==1) digitalWrite(RS, HIGH);
    else digitalWrite(RD, HIGH);
    Serial.print(type);
    Serial.println(" gram");
    float giatrido=scale.get_units(); 
    float error=0;
    while(true)
    {
      giatrido=scale.get_units()-ly;
      Serial.print(giatrido);
      Serial.println(" gram sữa đường");
      error=giatrido-sua;
      if((abs(error)<=saiso)||(error>=0)) break;
    }
    if(type==1) digitalWrite(RS, LOW);
    else digitalWrite(RD, LOW);
    Serial.println("Xong đường sữa");
    //---Bơm cofee
    digitalWrite(RCF, HIGH);
    giatrido=scale.get_units(); 
    error=0;
    while(true)
    {
      giatrido=scale.get_units()-ly;
      Serial.print(giatrido);
      Serial.println(" gram cofee ");
      error=giatrido-df;
      if((abs(error)<=saiso)||(error>=0)) break;
    }
    digitalWrite(RCF, LOW);
    ketthuc: 
    if(count<limit)
      Serial.println("Xong coffee");
    else Serial.println("Lỗi không ly");
    index=0;
    memset(buffer, 0, sizeof(buffer));
}
void setup() {
  // initialize serial:
  Serial.begin(115200);
  scale_setup();
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  _int_();
 // test_relay(5);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
//  #scale_data = scale.get_units();
 // #Serial.print("Trọng lượng bột:");
 // #Serial.println(scale_data);
    //Serial.println(sizeof(buffer));
  if (stringComplete) {
    //Serial.println(inputString);
    //Serial.println(index);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}
void serialEvent() {
  //index=0;
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    buffer[index-1] = inChar;
    Serial.println(buffer);
    inputString += inChar;
    if (inChar == '$') {
      stringComplete = true;
      buffer[index]='\0';
      //Serial.println("hello");
//      for(int i=0;i<=sizeof(buffer);i++)
//        {Serial.print(i);Serial.print(" ");
//        Serial.println(buffer[i]);}
      if (buffer[0] == 'S') {
        CS = strtol(buffer+1, NULL, 10); // Stringto long integer
        BomCofffee(1,CS,3); 
     }else  if (buffer[0] == 'D') {
        CD = strtol(buffer+1, NULL, 10); // Stringto long integer
        BomCofffee(2,CD,3);
     }else  if (buffer[0] == 'N') {
        NC = strtol(buffer+1, NULL, 10); // Stringto long integer
        Bomnuoc(3,NC,3);
     }else  if (buffer[0] == 'C') {
        CC = strtol(buffer+1, NULL, 10); // Stringto long integer
        Bomnuoc(3,CC,3);
      }
      index=0;
     }
     else index++;
  }
}
