#include <SPI.h>
#include <LoRa.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

static const int RXPin = 26, TXPin = 27;
static const uint32_t GPSBaud = 9600;
#define LORA_SS 5
#define LORA_RST 14
#define LORA_DI0 2 


TinyGPSPlus gps;
SoftwareSerial ss(RXPin, TXPin);

void setup() {
  Serial.begin(9600);
  LoRa.setPins(LORA_SS, LORA_RST, LORA_DI0);
  ss.begin(GPSBaud);
  LoRa.begin(433E6);
  LoRa.setTxPower(18);
}

void loop() {
  smartDelay(5000);

  if (gps.location.isValid()) {
    Serial.print(gps.location.lat(), 6);
    Serial.print(",");
    Serial.println(gps.location.lng(), 6);

    LoRa.beginPacket();
    LoRa.print(gps.location.lat(), 6);
    LoRa.print(",");
    LoRa.println(gps.location.lng(), 6);
    LoRa.endPacket();
  }
}

static void smartDelay(unsigned long ms) {
  unsigned long start = millis();
  do {
    while (ss.available())
      gps.encode(ss.read());
  } while (millis() - start < ms);
}
