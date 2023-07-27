void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(22, HIGH);// turn the LED on (HIGH is the voltage level)
                        // wait for a second
}
