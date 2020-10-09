#include <MKRWAN.h>
#include <CayenneLPP.h>
#include <pins_arduino.h>
//#include
#include <avr/io.h>


#include "ArduinoLowPower.h"


#include "arduino_secrets.h"

#include <OneWire.h>

//OneWire  ds(2);
OneWire  ds(A4);  // on pin 10 (a 4.7K resistor is necessary)

  byte i;
  byte present = 0;
  byte type_s;
  byte data[12];
  byte addr[8];
  float celsius;


CayenneLPP lpp(51);
LoRaModem modem;

String appEui = SECRET_APP_EUI;
String appKey = SECRET_APP_KEY;

#define CONST_VOLTAGE 0.2588235294117647

#define  TEMP_LED_D3 3

double val_temp = 20.00;
double val_hum = 50.00;
double val_batt = 99;

void setup() {
  pinMode(TEMP_LED_D3, OUTPUT);
  digitalWrite(TEMP_LED_D3, LOW);
  if (!modem.begin(EU868)) 
  errorBlink(3);
  int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) 
      errorBlink(4);
  
  modem.minPollInterval(60);
}
void loop() {
  digitalWrite(TEMP_LED_D3, LOW);
  val_batt = analogRead(32);
  val_batt = val_batt * CONST_VOLTAGE;


ds18b20_init();
float val_temp = ds18b20_read();

  lpp.reset();
  lpp.addTemperature(2, val_temp);
  
  int err;
  modem.beginPacket();
  modem.write(lpp.getBuffer(), lpp.getSize());
  err = modem.endPacket(false);
  digitalWrite(TEMP_LED_D3, HIGH);
  LowPower.sleep(INTERVAL);
  //delay(8000);
}


void errorBlink(int blink_delay)
{
  while (1)
  {
    for (int i = 0; i>blink_delay; i++)
    {
    digitalWrite(LED_BUILTIN, !digitalRead(2));
    delay(200);
    digitalWrite(LED_BUILTIN, !digitalRead(2));
    delay(200);
  }
  }
    delay(2000);
}



void ds18b20_init()
{
  if ( !ds.search(addr)) {
    ds.reset_search();
    delay(250);
    return;
  }
  }

float ds18b20_read()
{
  ds.reset();
  ds.select(addr);
  ds.write(0x44, 1);        // start conversion, with parasite power on at the end
  
  delay(1000);     // maybe 750ms is enough, maybe not
  
  present = ds.reset();
  ds.select(addr);    
  ds.write(0xBE);         // Read Scratchpad

  for ( i = 0; i < 9; i++) {           // we need 9 bytes
    data[i] = ds.read();
  }
  int16_t raw = (data[1] << 8) | data[0];
  if (type_s) {
    raw = raw << 3; // 9 bit resolution default
    if (data[7] == 0x10) {
      // "count remain" gives full 12 bit resolution
      raw = (raw & 0xFFF0) + 12 - data[6];
    }
  } else {
    byte cfg = (data[4] & 0x60);
    if (cfg == 0x00) raw = raw & ~7;  // 9 bit resolution, 93.75 ms
    else if (cfg == 0x20) raw = raw & ~3; // 10 bit res, 187.5 ms
    else if (cfg == 0x40) raw = raw & ~1; // 11 bit res, 375 ms
  }
  celsius = (float)raw / 16.0;
return celsius;
}
