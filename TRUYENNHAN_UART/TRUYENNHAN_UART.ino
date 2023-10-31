#include "HX711.h"
#include <TimeLib.h>
char buffer[10];
int index=1;
int ST=100,SD=100,NC=100;
float cup = 150;// một ly 150ml 
bool bom_vichat=0;
int Luongnuoc=150;
int tile_duong=0;

void setup() {
  // initialize serial:
  Serial.begin(115200);


}

void loop() {
  int a=18019;
  int b =a/100;
  int c=a%100;
  Serial.println(b);
  Serial.println(c);
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
      bom_vichat=0;
      buffer[index]='\0';
      //Serial.println("hello");
//      for(int i=0;i<=sizeof(buffer);i++)
//        {Serial.print(i);Serial.print(" ");
//        Serial.println(buffer[i]);}
      if (buffer[0] == 'S') {
        ST = strtol(buffer+1, NULL, 10); // Stringto long integer
        Serial.println(ST);
        if(ST>100){
          Serial.println("Bơm vi chất");
          bom_vichat=1;
          ST= ST-100;
        }
        Serial.println("Sữa tươi");
        Serial.println(ST);
        //bom(1,bom_vichat,ST);
        //BomCofffee(1,CS,3); 
      }else  if (buffer[0] == 'D') {
        SD = strtol(buffer+1, NULL, 10); // Stringto long integer
        Serial.println(SD);
        if(SD>100){
          Serial.println("Bơm vi chất");
          bom_vichat=1;
          SD= SD-100;
          }
        Serial.println("Sữa tươi");
        Serial.println(SD);
        //bom(1,bom_vichat,SD);
      }else  if (buffer[0] == 'C') {
        NC = strtol(buffer+1, NULL, 10); // Stringto long integer
        Serial.println(NC);
        if(NC>100){
          Serial.println("Bơm vi chất");
          bom_vichat=1;
          NC= NC-100;
          }
        Serial.println("Sữa tươi");
        Serial.println(NC);
        //bom(1,bom_vichat,NC);
      }
      index=0;
     }
     else index++;
  }
}

