#include <pop7.h>
#include <Wire.h>

byte dataCommand[2];

void setup() {
  glcdClear();
  Wire.begin(0x12);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
  pinMode(22, INPUT_PULLUP);
  //sw_OK_press();
  beep();
}
 void loop() {
  motor(1,dataCommand[0]-127);
  motor(2,dataCommand[1]-127);
  
}
void receiveEvent() 
{
  byteCount = 0;
  while (Wire.available())
  {
    dataCommand[byteCount]= Wire.read();
    byteCount++;
  }
  dataMode = int(dataCommand[0]);
  if (dataMode ==2)
  {
    glcd(int(dataCommand[1], int(dataCommand[2]), "%d"
  }
    
}
void requestEvent() {
  byte data = sw_OK();
  Wire.write(data);
  }
