
char buffer[11];
String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(115200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(buffer[2]);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
int numChar;
void serialEvent() {
  if (Serial.available() > 0) { // Check if data has beenentered
  int index=0;
  delay(100); // Let the buffer fill up
  int numChar = Serial.available(); // Find the stringlength
  if (numChar>10) {
  numChar=10;
  }
  while (numChar--) {
  // Fill the buffer with the string
  buffer[index++] = Serial.read();
  }
  buffer[index]='\0';
  splitString(buffer); // Run splitString function
  }
}
