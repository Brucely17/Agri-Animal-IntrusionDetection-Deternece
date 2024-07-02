
#include <Servo.h>
int Buzzerpin = 13;
#define trigPin 9
#define echoPin 10
// #define pirPin 7
// #define servoPin 6
Servo servoMotor;
Servo servoMotor1;
// #define buzzerPin 13

// Servo myservo;
int x;
int angleIncrement = 3;
void setup() {
  Serial.begin(9600);
   servoMotor.attach(6);
  servoMotor1.attach(8);
  pinMode(Buzzerpin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  // pinMode(pirPin, INPUT);
  // pinMode(servoPin, OUTPUT);
  // pinMode(buzzerPin, OUTPUT);
 
}

void loop() {
  long duration, distance;
  // int pirState = LOW;
  // digitalWrite(buzzerPin, LOW);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  // Serial.println(distance);
  delay(1000);
 

  if (distance < 20 && distance != 0) { // Adjust the distance threshold as needed
    
    // pirState = digitalRead(pirPin);
    // Serial.println("detected");

    // if (pirState == HIGH) {
    //   Serial.println("Motion detected!");
    //   // digitalWrite(LEDpin, HIGH);
    //   delay(5000);
    //   // Send value to indicate motion detected
      Serial.print(1);

    //   activateServo();
    //   delay(10000); // Stop for 10 seconds
    }

   else {
    servo_turn();
  }

  // Check if data is available from Python script
  // while(!Serial.available()) {};

    if (Serial.available()>0){
      

    x = Serial.read(); // Read the data from Python
    // Serial.print("Received from Python: ");
    // Serial.println(x); // Print the received value
    
    // Check if the received data indicates a dog (assuming 'd' for dog and 'p' for person)
    if (x == '0') {
      // Buzzer should work for a dog
      digitalWrite(Buzzerpin, HIGH);
      delay(8000);
      digitalWrite(Buzzerpin, LOW);


    } else if (x == '1') {
      // Buzzer should work for a person
      digitalWrite(Buzzerpin, LOW);
     
    }
  }
}




void servo_turn(){
  for (int angle = 0; angle <= 180; angle += angleIncrement) {
    servoMotor.write(angle);
    servoMotor1.write(angle);
    delay(20); // Adjust delay for smoother movement
  }


  // Gradually decrease angle increment as servo motors approach 360 degrees
  for (int angle = 180; angle >= 0; angle -= angleIncrement) {
    servoMotor.write(angle);
    servoMotor1.write(angle);
    delay(20); // Adjust delay for smoother movement
  }
}
