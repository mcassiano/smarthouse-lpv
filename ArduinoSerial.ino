char stringBuffer[500];

void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);

}

void loop() {
    // put your main code here, to run repeatedly:
    if (Serial.available()) {
        int i = readCommand(stringBuffer);
        Serial.print(stringBuffer);
        Serial.print(", ");
        Serial.println(i);
    }
    
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
