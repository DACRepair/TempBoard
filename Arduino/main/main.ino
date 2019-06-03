#include <Arduino.h>
#include <OneWire.h>
#include <DallasTemperature.h>


#define ONE_WIRE_BUS 12


OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
DeviceAddress DS18B20[3];

void setup(void)
{
  Serial.begin(115200);

  sensors.begin();

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}

void loop(void)
{
  byte i;
  byte addr[8];

  // LED flashes at polling rate.
  digitalWrite(LED_BUILTIN, LOW);
  sensors.setWaitForConversion(false);
  while (oneWire.search(addr))
  {
    // Set up device
    sensors.setResolution(addr, 12);
    sensors.requestTemperaturesByAddress(addr);

    // Send Device Address
    for (i = 0; i < 8; i++)
    {
      Serial.write(addr[i]);
    }

    //  ADDR / Temp Separator
    Serial.write(0x91);

    // Get and send temp
    uint16_t t = sensors.getTemp(addr);
    Serial.write((t >> 8) & 0xFF);
    Serial.write((t & 0xFF));

    // Sensor separator
    Serial.write(0x92);
  }

  // Packet Terminator
  Serial.write(0x23);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(999);
}