#include <Arduino.h>

#define FORWARD 12
#define BACKWARD 11
#define RIGHT 10

const String pins[3] = {"FORWARD", "BACKWARD", "RIGHT"};

//driver's engines pins
const int right_forward[2] = {6, 10}; // pins to move the right engine forward
const int left_forward[2] = {8, 12}; // pins to move the left engine forward
const int right_backward[2] = {7, 2}; // pins to move the right engine backward
const int left_backward[2] = {9, 11}; // pins to move the left engine backward
const int right_stop[2] = {10, 2}; // pins to stop the right engine
const int left_stop[2] = {12, 11}; // pins to stop the left engine
const int right_speed_pin = 3;
const int left_speed_pin = 5; 

int right_velocity = 0; // this is the value that will control de PWM of the L298 that will drive the mosfet of the right engine
int left_velocity = 0; // this is the value that will control de PWM of the L298 that will drive the mosfet of the left engine

boolean forward_status = LOW;
boolean backward_status = LOW;
boolean right_status = LOW;

// Prototypes
void turnOffDriver(void);
void moveForward(void);
void moveBackward(void);
void moveRight(void);
void moveLeft(void);
void speedUp(void);
void speedDown(void);
void stop(void);

void setup() {
  Serial.begin(9600);

   // config as OUTPUT the pins that drives the relays
  for (int i = 0; i < 2; i++)
  {
    pinMode(right_forward[i], OUTPUT);
    pinMode(right_backward[i], OUTPUT);
    pinMode(left_forward[i], OUTPUT);
    pinMode(left_backward[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.println(data);
    
    if(data.compareTo("forward") == 0) // if the strings are equals return 0
    {
      moveForward();
    }

    else if(data.compareTo("backward") == 0) // if the strings are equals return 0
    {
      moveBackward();
    }

    else if(data.compareTo("right") == 0) // if the strings are equals return 0
    {
      moveRight();
    }

    else if(data.compareTo("left") == 0) // if the strings are equals return 0
    {
      moveLeft();
    }

    else if(data.compareTo("stop") == 0) // if the strings are equals return 0
    {
      stop();
    }

    else if(data.compareTo("speed up") == 0) // if the strings are equals return 0
    {
      speedUp();
    }

    else if(data.compareTo("speed down") == 0) // if the strings are equals return 0
    {
      speedDown();
    }

  }
}

// --------------------- Definitions ----------------------

void turnOffDriver(void)
{
  for(int i=0; i<2; i++)
  {
    digitalWrite(right_forward[i], LOW);
    digitalWrite(left_forward[i], LOW);
    digitalWrite(right_backward[i], LOW);
    digitalWrite(left_backward[i], LOW);
  }

  right_velocity = left_velocity = 0;

  analogWrite()
}

void moveForward(void)
{
  turnOffDriver();

  for(int i=0; i<2; i++)
  {
    digitalWrite(right_forward[i], HIGH);
    digitalWrite(left_forward[i], HIGH);
  }
}

void moveBackward(void)
{
  turnOffDriver();

  for(int i=0; i<2; i++)
  {
    digitalWrite(right_backward[i], HIGH);
    digitalWrite(left_backward[i], HIGH);
  }
}

void moveRight(void)
{
  turnOffDriver();

  for (int i = 0; i < 2; i++)
  {
    digitalWrite(right_backward[i], HIGH);
    digitalWrite(left_forward[i], HIGH);
  }
}

void moveLeft(void)
{
  turnOffDriver();

  for (int i = 0; i < 2; i++)
  {
    digitalWrite(right_forward[i], HIGH);
    digitalWrite(left_backward[i], HIGH);
  }
}

void speedUp(void)
{
  if (right_velocity >= 250 || left_velocity >= 250)
  {
    right_velocity = left_velocity = 250;
  }
  else
  {
    right_velocity += 50;
    left_velocity += 50;
  }
}

void speedDown(void)
{
  if (right_velocity <= 50 || left_velocity <= 250)
  {
    right_velocity = left_velocity = 50;
  }
  else
  {
    right_velocity -= 50;
    left_velocity -= 50;
  }
}

void stop(void)
{
  turnOffDriver();

  for (int i = 0; i < 2; i++)
  {
    digitalWrite(right_stop[i], HIGH);
    digitalWrite(left_stop[i], HIGH);
  }
  
}



