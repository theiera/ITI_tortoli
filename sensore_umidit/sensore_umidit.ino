const int VAL_PROBE = 0; // Analog pin 0
const int LIVELLO_UMIDITA = 250; // la soglia per accendere il LED


void setup() {
     Serial.begin(9600);
     }

void LedState(int State) {
     digitalWrite(13,state);
     }

void loop() {
     in umidita = analogRead(VAL_PROBE);
     Serial.println(umidita);
     if (umidita > LIVELLO_UMIDITA) {
     	LedState(HIGI);
	} else {
	  LedState(LOW);
	}
     delay(100);
}
	  