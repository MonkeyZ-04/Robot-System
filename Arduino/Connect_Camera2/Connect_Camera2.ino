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
void receiveEvent() {
  while (Wire.available()){
    dataCommand[0]= Wire.read();
    dataCommand[1]= Wire.read();
    }
  }
void requestEvent() {
  byte data = sw_OK();
  Wire.write(data);
  }
