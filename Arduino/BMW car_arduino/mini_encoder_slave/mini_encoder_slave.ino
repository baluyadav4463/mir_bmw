#include <Wire.h>
#include <ros.h>
#include <std_msgs/UInt16.h>
#include<geometry_msgs/Vector3.h>
#include "Define.h"
//Creation of a NodeHandle // ros::NodeHandle_<HardwareType, MAX_PUBLISHERS=25, MAX_SUBSCRIBERS=25, IN_BUFFER_SIZE=512, OUT_BUFFER_SIZE=512> nh;   
ros::NodeHandle_<ArduinoHardware, 2, 2, 128, 128> nh;
//ros::NodeHandle  nh;
geometry_msgs::Vector3 data;

void manualCb( const std_msgs::UInt16& msg){
command=msg.data; 
manualCmd ();
}
ros::Subscriber<std_msgs::UInt16>  sub("Control", &manualCb);
ros::Publisher pos("pos",&data);

void setup() {
  nh.getHardware()->setBaud(57600);
  Wire.begin(8);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
  pinMode(2, INPUT);           // set pin to input
  pinMode(3, INPUT);           // set pin to input
  digitalWrite(2, HIGH);       
  digitalWrite(3, HIGH);       
  attachInterrupt(0, ai0, RISING);
  attachInterrupt(1, ai1, RISING);
  pinMode(EnablePin1, OUTPUT);
  pinMode(EnablePin2, OUTPUT);
  pinMode(PWMPinA1, OUTPUT);
  pinMode(PWMPinB1, OUTPUT);
  pinMode(PWMPinA2, OUTPUT);
  pinMode(PWMPinB2, OUTPUT);
  digitalWrite(EnablePin1, LOW);
  digitalWrite(EnablePin2, LOW); 
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(pos);
}

void loop() {
   digitalWrite(EnablePin1, HIGH);
  digitalWrite(EnablePin2, HIGH); 
  count=map(counter,-561,561,-100,100);
  data.y=count;
  manualCmd();
  delay(40);
  pos.publish(&data);
  nh.spinOnce();
  delay(25);

}

void receiveEvent(int howMany) {
  while (1 < Wire.available()) { // loop through all but the last
    char  x = Wire.read();
  }
  int  c = Wire.read();
  data.x=c;
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
