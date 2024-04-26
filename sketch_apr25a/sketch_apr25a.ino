#include <Arduino_HS300x.h>

void setup() {
  Serial.begin(115200); 
  HS300x.begin();
}

void loop() {

  // read all the sensor values
  float temperature = HS300x.readTemperature();
  float humidity    = HS300x.readHumidity();

  Serial.print(temperature);
  Serial.print(",");
  Serial.println(humidity);

  // wait 1 second to print again
  delay(1000);

 }