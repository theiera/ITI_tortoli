const int VAL_PROBE = A0; // Analog pin 0
const int LIVELLO_Pioggia = 250; // la soglia per accendere il LED
void setup() {
     Serial.begin(9600);
     }
void loop() {
     int pioggia = analogRead(VAL_PROBE);
     Serial.println(pioggia);
     delay(100);
}