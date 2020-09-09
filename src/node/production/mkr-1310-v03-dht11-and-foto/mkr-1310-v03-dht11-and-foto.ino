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

#include "DHT.h"

#define DHTPIN 3
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

double val_temp = 20.00;
double val_hum = 50.00;
double val_batt = 99;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  dht.begin();
  if (!modem.begin(EU868))
  {
    errorBlink(3);
  }
  int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) {
    errorBlink(4);
  }
  modem.minPollInterval(60);

  digitalWrite(LED_BUILTIN, LOW);
}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  getDataFromDHT();
  val_batt = analogRead(A2);

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

void getDataFromDHT()
{
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  val_hum = dht.readHumidity();
  // Read temperature as Celsius (the default)
  val_temp = dht.readTemperature();
}


void errorBlink(int blink_delay)
{
  while (1)
  {
    for (int i = 0; i > blink_delay; i++)
      digitalWrite(LED_BUILTIN, !digitalRead(2));
    delay(200);
    digitalWrite(LED_BUILTIN, !digitalRead(2));
    delay(200);
  }
  delay(2000);
}
