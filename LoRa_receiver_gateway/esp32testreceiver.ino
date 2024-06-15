#include <SPI.h>
#include <LoRa.h>
#define LORA_SS 5
#define LORA_RST 14
#define LORA_DI0 2 

void setup() {
  Serial.begin(9600);
  LoRa.setPins(LORA_SS, LORA_RST, LORA_DI0);
  while (!Serial);

  Serial.println("LoRa Receiver");

  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  LoRa.setTxPower(18);
  LoRa.setSignalBandwidth(125E3);
  LoRa.setSpreadingFactor(10);
  LoRa.setSyncWord(0xF3);
  LoRa.enableCrc();
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {

    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }

  }
}
