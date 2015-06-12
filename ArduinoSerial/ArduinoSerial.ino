
#define COMMON_ANODE

int redPin = 9;
int greenPin = 10;
int bluePin = 11;
int tempPin = A1;

char stringBuffer[500];


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
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
        processCommand(stringBuffer);
    }
    
}

void processCommand(char* stringBuffer) {
  char s[32];
  strcpy(s, stringBuffer);
  char* token = strtok(s, " ");
  
  if (strcmp(token, "rgb") == 0) {
    int rgb[3];
    
    for (int i = 0; i < 3; i++) {
      token = strtok(NULL, " ");
      
      if (strcmp(token, "state") == 0) {
        getRGBColor();
        return;
      }  
      
      rgb[i] = atoi(token);
    }
    
    mudaCorRGB(rgb[0], rgb[1], rgb[2]);
  }
  
  else if (strcmp(token, "led") == 0) {
    int led;
    
    token = strtok(NULL, " ");
    
    if (strcmp(token, "state") == 0) {
      token = strtok(NULL, " ");
      led = atoi(token);
      int state = ledState(led);
      
      if (state == HIGH)
        Serial.print("{'status': 'OK', 'state': 'on'}\n");
      else
        Serial.print("{'status': 'OK', 'state': 'off'}\n");
        
      return;
    }
    
    led = atoi(token);
    toggleLed(led);
  }
  
  else if (strcmp(token, "temp") == 0) {
    readTemperature();
  }
  
}

void readTemperature() {
    
  int val = analogRead(tempPin);
  float cel = val*0.322265625;
        
  Serial.print("{'temperature': ");
  Serial.print(cel);
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

void getRGBColor() {
  
  int red = 255 - analogRead(redPin);
  int green = 255 - analogRead(greenPin);
  int blue = 255 - analogRead(bluePin);
  
  Serial.print("{'status': 'OK'}");
//  Serial.print("'color': '{'");
//  Serial.print("'red': ");
//  Serial.print(red);
//  Serial.print(", 'green': ");
//  Serial.print(green);
//  Serial.print(", 'blue': ");
//  Serial.print(blue);
//  Serial.print("}}\n");
  
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
