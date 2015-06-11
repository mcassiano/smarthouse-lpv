#include "DHT.h"

#define DHTPIN A2
#define DHTTYPE DHT11
#define COMMON_ANODE

int redPin = 9;
int greenPin = 10;
int bluePin = 11;

DHT dht(DHTPIN, DHTTYPE);

char stringBuffer[500];


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //dht.begin();
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
    //delay(2000);
    // put your main code here, to run repeatedly:
    if (Serial.available()) {
        int i = readCommand(stringBuffer);
        tokenize(stringBuffer);
    }
    
}

void tokenize(char* stringBuffer) {
  char s[32];
  strcpy(s, stringBuffer);
  char* token = strtok(s, " ");
  
  if (strcmp(token, "rgb") == 0) {
    int rgb[3];
    
    for (int i = 0; i < 3; i++) {
      token = strtok(NULL, " ");
      rgb[i] = atoi(token);
    }
    
    mudaCorRGB(rgb[0], rgb[1], rgb[2]);
  }
  
  else if (strcmp(token, "led") == 0) {
    int led;
    
    token = strtok(NULL, " ");
    led = atoi(token);
    
    toggleLed(led);
  }
}

void readTemperature() {
  
  float t = dht.readTemperature(); //70.4;
  float h = dht.readHumidity(); //23;
        
  Serial.print("{'temperature': ");
  Serial.print(t);
  Serial.print(", 'humidity': ");
  Serial.print(h);
  Serial.print("}\n");
  
}

void toggleLed(int led) {
  digitalWrite(led, !digitalRead(led));
  Serial.print("{'status': 'OK'}\n");
}

int ledState(int led) {
  return digitalRead(led);
}

void mudaCorRGB(int red, int green, int blue) {
 #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
 #endif
 
 analogWrite(redPin, red);
 analogWrite(greenPin, green);
 analogWrite(bluePin, blue);
 
 Serial.print("{'status': 'OK'}\n");
}

int readCommand(char *command) {
    int bufferSize = 0;
    
    stringBuffer[0] = '\0';
    char charBuffer;

    while (Serial.available()) {
        delay(3);
        if (Serial.available() > 0 &&
          (charBuffer = Serial.read()) != '\n') {
            stringBuffer[bufferSize] = charBuffer;
            stringBuffer[++bufferSize] = '\0'; 
        }
    }
    
    return bufferSize;
}
