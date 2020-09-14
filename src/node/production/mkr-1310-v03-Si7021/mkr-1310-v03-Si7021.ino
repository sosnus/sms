
#include <CayenneLPP.h>
#include <pins_arduino.h>

#include <MKRWAN.h>
#include "Adafruit_Si7021.h"
#include "ArduinoLowPower.h"
#include <avr/io.h>

#include "arduino_secrets.h"

CayenneLPP lpp(51);

Adafruit_Si7021 sensor = Adafruit_Si7021();

LoRaModem modem;

String appEui = SECRET_APP_EUI;
String appKey = SECRET_APP_KEY;

#define INTERVAL  300*1000
// interval in milliseconds

#define CONST_VOLTAGE 0.2588235294117647

void setup() {
  if (!modem.begin(EU868)) 
  {
  errorBlink(3);
  }

  int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) 
      errorBlink(4);

      if (!sensor.begin()) {
    errorBlink(5);
  }
  
  modem.minPollInterval(60);
}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);


  lpp.reset();
  
    lpp.addTemperature(2, sensor.readTemperature());
  lpp.addRelativeHumidity(3, sensor.readHumidity());
  
  int err;
  modem.beginPacket();
  modem.write(lpp.getBuffer(), lpp.getSize());
  err = modem.endPacket(false);
  digitalWrite(LED_BUILTIN, LOW);
  //LowPower.sleep(10000);
  delay(INTERVAL);
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
