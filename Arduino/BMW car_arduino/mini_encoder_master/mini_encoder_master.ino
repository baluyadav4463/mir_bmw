#include <Wire.h> //sender //black//master
 //This variable will increase or decrease depending on the rotation of encoder
int counter=0;
void setup() {
  Wire.begin();
  pinMode(2, INPUT);           // set pin to input
  pinMode(3, INPUT);           // set pin to input
  digitalWrite(2, HIGH);       
  digitalWrite(3, HIGH);       
  attachInterrupt(0, ai0, RISING);
  attachInterrupt(1, ai1, RISING);
}



void loop() {
  
  byte count=map(counter,0,65535,0,255);
  Wire.beginTransmission(8);
  Wire.write(count);
  Wire.endTransmission();
  delay(60);
}

void ai0() {

  if(digitalRead(3)==LOW) {
    counter++;
  }else{
    counter--;
  }
}

void ai1() {
  
  if(digitalRead(2)==LOW) {
    counter--;
  }else{
    counter++;
  }
}
