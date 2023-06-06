#include<ESP8266WiFi.h>
#include<DHT.h>
#include<WiFiClient.h>
#include<ThingSpeak.h>

const char* ssid="";//Your network SSID
const char* password="";//Your Network password
WiFiClient client;
unsigned long myChannelNumber=; // Channel code
const char* myWriteAPIKey="";//Your API key

int vib_pin=D1; // D1
int timer = 0;
int lm = 0;

void setup() {
  pinMode(vib_pin,INPUT);
  Serial.begin(9600);
  Serial.println("COnnected");
   //Connect to WIFI Network
  WiFi.begin(ssid,password);
  ThingSpeak.begin(client);

}

void loop() {
  if(timer>200){
    Serial.println();
    if(lm>20){
      lm = 20;
    }
    Serial.println(lm);
    ThingSpeak.writeField(myChannelNumber, 1,lm,myWriteAPIKey);
    timer = 0;
    lm = 0;
    
   }
  else{
    timer++;
    delay(50);
    int val=digitalRead(vib_pin);
    if(val==0){
      lm++;
    }
    Serial.print(val);
  }
}
