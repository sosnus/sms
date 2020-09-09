#include <MKRWAN.h>
#include <CayenneLPP.h>
#include <pins_arduino.h>
//#include
#include <avr/io.h>

#include "arduino_secrets.h"

CayenneLPP lpp(51);
LoRaModem modem;

String appEui = SECRET_APP_EUI;
String appKey = SECRET_APP_KEY;

#define CONST_VOLTAGE 0.2588235294117647

double val_temp = 20.00;
double val_hum = 50.00;
double val_batt = 99;

void setup() {
  if (!modem.begin(EU868)) 
  errorBlink(3);
  int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) 
      errorBlink(4);
  
  modem.minPollInterval(60);
}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  val_batt = analogRead(32);
  val_batt = val_batt * CONST_VOLTAGE;

  lpp.reset();
  lpp.addAnalogInput(1, val_batt);
  lpp.addTemperature(2, val_temp);
  lpp.addRelativeHumidity(3, val_hum);
  
  int err;
  modem.beginPacket();
  modem.write(lpp.getBuffer(), lpp.getSize());
  err = modem.endPacket(false);
  digitalWrite(LED_BUILTIN, LOW);
  //LowPower.sleep(10000);
  delay(8000);
}


void errorBlink(int blink_delay)
{
  while (1)
  {
    for (int i = 0; i>blink_delay; i++)
    digitalWrite(LED_BUILTIN, !digitalRead(2));
    delay(200);
    digitalWrite(LED_BUILTIN, !digitalRead(2));
    delay(200);
  }
    delay(2000);
}
