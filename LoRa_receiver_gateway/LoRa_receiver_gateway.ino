#include <SPI.h>
#include <LoRa.h>

#define LORA_SS 15 
#define LORA_RST 16 
#define LORA_DI0 4 

void setup() {
  Serial.begin(9600);
  LoRa.setPins(LORA_SS, LORA_RST, LORA_DI0);
 
  while (!Serial);


  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
 
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    
    Serial.print("Received packet '");

   
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }

  
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}
