#include <Keypad.h>

const int ROW_NUM = 3; //four rows
const int COLUMN_NUM = 5; //three columns

char keys[ROW_NUM][COLUMN_NUM] = {
  {'+','9','8','7','c'},
  {'-','6','5','4','p'},
  {'0','3','2','1','k'}  
};

byte pin_rows[ROW_NUM] = {11, 10, 9}; //connect to the row pinouts of the keypad
byte pin_column[COLUMN_NUM] = {6, 5, 4, 3, 2}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), pin_rows, pin_column, ROW_NUM, COLUMN_NUM );

void setup(){
  Serial.begin(9600);
}

void loop(){
  char key = keypad.getKey();

  if (key){
    Serial.print(key);
    delay(200);
  }
}
