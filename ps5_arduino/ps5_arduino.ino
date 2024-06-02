void setup() {
    Serial.begin(115200);  // Initialize serial communication at 9600 baud
    // Initialize your motor control pins here
    // For example:
    // pinMode(motorPin1, OUTPUT);
    // pinMode(motorPin2, OUTPUT);
}

void loop() {
    if (Serial.available()) {
        String data = Serial.readStringUntil('\n');  // Read incoming data until newline character
        int firstComma = data.indexOf(',');
        String eventType = data.substring(0, firstComma);

        if (eventType == "KEY") {
            int secondComma = data.indexOf(',', firstComma + 1);
            int scancode = data.substring(firstComma + 1, secondComma).toInt();
            int keystate = data.substring(secondComma + 1).toInt();
            // Process the key event (scancode, keystate)
           Serial.print("Key Event - Scancode: ");
            Serial.print(scancode);
           Serial.print(", Keystate: ");
          Serial.println(keystate);
        //Add your motor control logic based on key events here
//           if(scancode == 17 && keystate == -1){
//            Serial.print("pad up");
//        }
//        else{
//          Serial.print("pad down");
//        }
//        
        
         } else if (eventType == "ABS") {
            int secondComma = data.indexOf(',', firstComma + 1);
            int code = data.substring(firstComma + 1, secondComma).toInt();
            int value = data.substring(secondComma + 1).toInt();
            // Process the absolute axis event (code, value)
        Serial.print("ABS Event - Code: ");
       Serial.print(code);
          Serial.print(", Value: ");
          Serial.println(value);
            // Add your motor control logic based on joystick values here
  
             if(code == 17 && value == -1){
            Serial.println("pad up");
        }
            else if(code == 17 && value == 1){
           Serial.println("pad down");
      }
        }
    }
}
