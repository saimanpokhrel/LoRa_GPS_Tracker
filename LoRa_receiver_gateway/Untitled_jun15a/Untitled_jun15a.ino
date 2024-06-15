
#include "arduino_secrets.h"

#include "thingProperties.h"
#include <SPI.h>
#include <LoRa.h>

#define LORA_SS 5
#define LORA_RST 14
#define LORA_DI0 2 

void setup() {
  // Initialize serial and wait for port to open:
  Serial.begin(9600);
   LoRa.setPins(LORA_SS, LORA_RST, LORA_DI0);

 LoRa.begin(433E6);
  delay(1500); 

  // Defined in thingProperties.h
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
  
  LoRa.setTxPower(18);
  LoRa.setSignalBandwidth(125E3);
  LoRa.setSpreadingFactor(10);
  LoRa.setSyncWord(0xF3);
  LoRa.enableCrc();
}

void loop() {
  ArduinoCloud.update();
  if (LoRa.parsePacket()) {
    while (LoRa.available()) {
      String receivedData = LoRa.readString();

      int commaIndex = receivedData.indexOf(',');
      if (commaIndex != -1) {
        String latString = receivedData.substring(0, commaIndex);
        String lonString = receivedData.substring(commaIndex + 1);

        float latitude = latString.toFloat();
        float longitude = lonString.toFloat();

        // Set the CloudLocation variable x with the extracted latitude and longitude
       x = Location(latitude,longitude);

        // Report the values to IoT Cloud
        ArduinoCloud.update();

      }
    }
  }
}
