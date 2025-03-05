/*
  Analog Input

 http://arduino.cc/en/Tutorial/AnalogInput
 
 */

int sensorPin1 = A0;    // select the input pin for the IR 1
int sensorPin2 = A1;    // select the input pin for the IR 2
int ledPin1 = 12;      // select the pin for the rasp IR 1
int ledPin2 = 13;      // select the pin for the rasp IR 2
int sensorValue1 = 0;  // variable to store the value coming from the sensor 1
int sensorValue2 = 0;  // variable to store the value coming from the sensor 2

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin1, OUTPUT);  
  pinMode(ledPin2, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensor:
  sensorValue1 = analogRead(sensorPin1);  
  sensorValue2 = analogRead(sensorPin2);   
  if (sensorValue1 >= 118) {
    digitalWrite(ledPin1, LOW);
    }
  else {
    digitalWrite(ledPin1, HIGH);
      }
  if (sensorValue2 >= 118) {
    digitalWrite(ledPin2, LOW);
    }
  else {
    digitalWrite(ledPin2, HIGH);
      }   
   Serial.println(sensorValue1);               
}
