int latchPin = 11;
int clockPin = 9;
int dataPin = 12;
byte low = 0;
byte high = 0;
byte leds = 0;
int num;
void updateShiftRegister(unsigned int low, unsigned int high){
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, low);
  shiftOut(dataPin, clockPin, LSBFIRST, high);
  digitalWrite(latchPin, HIGH);
}



void setup(){
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
}

void one(){
  high = 0b01100000;
}

void two(){
  high = 0b11011011;
}

void three() {
  high = 0b11110011;
}

void four() {
  high = 0b01100111;
}

void five() {
  high = 0b10110111;
}

void six() {
  high = 0b10111111;
}

void seven(){
  high = 0b11100000;
}

void eight(){
  high = 0b11111111;
}

void nine() {
  high = 0b11110111;  
}

void zero(){
  high = 0b11111101;
}

void numberCheck(){
  if (num==1){
    one();
  }
  if (num==2){
    two();
  }
  if (num==3){
    three();
  }
  if (num==4){
    four();
  }
  if (num==5){
    five();
  }
  if (num==6){
    six();
  }
  if (num==7){
    seven();
  }
  if (num==8){
    eight();
  }
  if (num==9){
    nine();
  }
  if(num==0){
    zero();
  }
}

void loop(){
  low = 0b01111111;
  one();
  updateShiftRegister(low, high);
  delay(1);
  low = 0b10111111;
  two();
  updateShiftRegister(low, high);
  delay(1);
  low=0b11011111;
  three();
  updateShiftRegister(low, high);
  delay(1);
  low=0b11101111;
  four();
  updateShiftRegister(low, high);
  delay(1);
  
  
}
