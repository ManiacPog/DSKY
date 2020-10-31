int latchPin = 11;
int clockPin = 9;
int dataPin = 12;
byte first;
byte second;
byte third;



void updateShiftRegister(){
  digitalWrite(latchPin, LOW);
  
  shiftOut(dataPin, clockPin, LSBFIRST, first);
  shiftOut(dataPin, clockPin, LSBFIRST, second);  
  shiftOut(dataPin, clockPin, LSBFIRST, third);  
  digitalWrite(latchPin, HIGH);
}



void setup(){
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  Serial.begin(9600);
  
}

void setNumber(int num){
  if (num == 1){
    third = 0b01100000;
    second = 0b01100000;
  }

  if (num == 2){
    third = 0b11011011;
    second = 0b11011011;
  }

  if (num == 3){
    third = 0b11110011;
    second = 0b01100000;
  }

  if (num == 4){
    third = 0b01100111;;
    second = 0b01100111;;
  }

  if (num == 5){
    third = 0b10110111;
    second = 0b10110111;
  }

  if (num == 6){
    third = 0b10111111;
    second = 0b10111111;
  }

  if (num == 7){
    third = 0b11100001;
    second = 0b11100001;
  }
  if (num == 8){
    third = 0b11111111;
    second = 0b11111111;
  }
  if (num == 9){
    third = 0b11100111;
    second = 0b11110111;
  }
  if (num == 0){
    third = 0b11111101;
    second = 0b11111101;
  }
}

void loop(){
  
  first = 0b01111111;
  setNumber(2);
  updateShiftRegister();
  delay(1);
  first = 0b10111111;
  setNumber(3);
  updateShiftRegister();
  delay(1);
  first = 0b11011111;
  setNumber(4);
  updateShiftRegister();
  delay(1);
  first = 0b11101111;
  setNumber(5);
  updateShiftRegister();
  delay(1);
  first = 0b11110111;
  setNumber(0);
  updateShiftRegister();
  delay(1);
}
