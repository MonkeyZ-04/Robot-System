#include <pop7.h>
#include <Wire.h>

byte dataCommand[4];

void setup() {
  glcdClear();
  Serial1.begin(115200);
  Wire.begin(0x12);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
  pinMode(22, INPUT_PULLUP);
  //sw_OK_press();
  beep();
}

void loop() 
{
  char serialData = 0;  
   if (Serial1.available()) serialData = Serial1.read();
   if(serialData == '1'){
//    motor_stop(ALL);
    beep();
    glcd(0,0,"Drop 1");
//    delay(2000); 
  }
   else if(serialData == '2')
  {
//    motor_stop(ALL);
    beep();
    glcd(0,0,"Drop 2");
//    delay(2000); 
  }
    else if(serialData == '3')
  {
//    motor_stop(ALL);
    beep();
    glcd(0,0,"Drop 3");
//    delay(2000); 
  }
   else if(serialData == '4')
  {
//    motor_stop(ALL);
    beep();
    glcd(0,0,"Drop 4");
//    delay(2000); 
  }
   else if(serialData == '5')
  {
//    motor_stop(ALL);
    beep();
    glcd(0,0,"Drop 5");
//    delay(2000); 
  }
   else
  {
  motor(1, dataCommand[1]-127);
  motor(2, dataCommand[0]-127);
  motor(3, dataCommand[2]-127);
  motor(4, dataCommand[3]-127);
  }
}

void receiveEvent(){
  while(Wire.available()){
    dataCommand[0] = Wire.read();
    dataCommand[1] = Wire.read();
    dataCommand[2] = Wire.read();
    dataCommand[3] = Wire.read();
  }
}

void requestEvent(){
  byte data = sw_OK();
  Wire.write(data);
}
