void cali(){

if ( count<0 && count < -7)
  steer='R';

if (count >0 && count>7)
  steer='L';

if (count>-7 && count<7)
  steer='S';

while (steer!='S'){
 
if (steer =='L')
{    analogWrite(PWMPinB1, 0);
     analogWrite(PWMPinA1, 180);
     delay(50);
     analogWrite(PWMPinA1, 80);
     break;
     }
if (steer =='R')
{    analogWrite(PWMPinB1, 180);
     analogWrite(PWMPinA1, 0);
     delay(50);
     analogWrite(PWMPinA1, 80);
     break;
     }
}

analogWrite(PWMPinB1, 0);
analogWrite(PWMPinA1, 0);
}
