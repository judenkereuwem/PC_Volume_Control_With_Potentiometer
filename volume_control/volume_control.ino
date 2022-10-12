
const int potPin = A0;
int mapped_value;
int pot_value;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // reading from potentiometer
  pot_value = analogRead(potPin);

  // Mapping the Values between 0 to 255 
  mapped_value = map(pot_value, 0, 1023, 0, 100);

  // send values to serial monitor
  Serial.println(mapped_value);
  delay(100);
}
