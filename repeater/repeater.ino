#include <SPI.h>
#include <LoRa.h>

const int csPin = 10;
const int resetPin = 9;
const int dio0Pin = 2;

String receivedData;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Receiver and Repeater");
  LoRa.setPins(csPin, resetPin, dio0Pin);

  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  Serial.println("LoRa Initializing OK!");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    Serial.print("Received packet '");

    while (LoRa.available()) {
      receivedData += (char)LoRa.read();
    }

    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());

    retransmitData(receivedData);
    receivedData = "";
  }
}

void retransmitData(String data) {
  Serial.print("Retransmitting packet: ");
  Serial.println(data);

  LoRa.beginPacket();
  LoRa.print(data);
  LoRa.endPacket();
}
