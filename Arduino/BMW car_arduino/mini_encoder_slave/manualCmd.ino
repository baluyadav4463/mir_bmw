
void manualCmd()
{
  switch(command)
  {
    case 0:
     analogWrite(PWMPinB1, 0);
     analogWrite(PWMPinA1, 0);
     analogWrite(PWMPinB2, 0);
     analogWrite(PWMPinA2, 0);
     state=command;
     break;
    case 4:
     if(count>90){
     analogWrite(PWMPinB1, 0);
     analogWrite(PWMPinA1, 0);
     }
     else {
     analogWrite(PWMPinB1, 150);
     analogWrite(PWMPinA1, 0);
     delay(100);
     analogWrite(PWMPinB1, 0);
     analogWrite(PWMPinA1, 0);}
     
     state=command;
     break;
    case 6:
     if(count<-100){
     analogWrite(PWMPinB1, 0);
     analogWrite(PWMPinA1, 0);
     }
     else {
     analogWrite(PWMPinB1, 0);
     analogWrite(PWMPinA1, 150);
     delay(100);
     analogWrite(PWMPinB1, 0);
     analogWrite(PWMPinA1, 0);}
     state=command;
     break;
    case 8:
     analogWrite(PWMPinB2, 0);
     analogWrite(PWMPinA2, duty);
     state=command;
     break;
    case 2:
     analogWrite(PWMPinB2, 100);
     analogWrite(PWMPinA2, 0);
     state=command;
     break;
    case 5: 
      if (state == 8)
      {
        duty = duty + 10;
        if (duty > MAX_SPEED) 
        { 
          duty = MAX_SPEED;
        }  
        command = 8;
      } else {command = state;}
      break;

    case 9: 
      if (state == 8)
      {
        duty = duty - 10;
      }     
      if (duty < MIN_SPEED ) 
      { 
        duty = MIN_SPEED;
      }
      command = state;
      break;
      
    case 7:
      cali();
      state=command;
      break;  
}

 if(count>90 || count <-100){
  analogWrite(PWMPinB1, 0);
  analogWrite(PWMPinA1, 0);}
}
