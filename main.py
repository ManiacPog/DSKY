#DSKY Server
import pyautogui as pg
import serial
import time

pg.FAILSAFE = False

def enterKey(num):
    if num == 1:
        pg.keyDown('ctrl')
        pg.keyDown(f'num1')
        pg.keyUp('ctrl')
        pg.keyUp(f'num1')
    if num == 2:
        pg.keyDown('ctrl')
        pg.keyDown(f'f2')
        pg.keyUp('ctrl')
        pg.keyUp(f'f2')
    if num == 3:
        pg.keyDown('ctrl')
        pg.keyDown(f'f3')
        pg.keyUp('ctrl')
        pg.keyUp(f'f3')
    if num == 4:
        pg.keyDown('ctrl')
        pg.keyDown(f'f4')
        pg.keyUp('ctrl')
        pg.keyUp(f'f4')
    if num == 5:
        pg.keyDown('ctrl')
        pg.keyDown(f'f5')
        pg.keyUp('ctrl')
        pg.keyUp(f'f5')
    if num == 6:
        pg.keyDown('ctrl')
        pg.keyDown(f'f6')
        pg.keyUp('ctrl')
        pg.keyUp(f'ff6')
    if num == 7:
        pg.keyDown('ctrl')
        pg.keyDown(f'f7')
        pg.keyUp('ctrl')
        pg.keyUp(f'f7')
    if num == 8:
        pg.keyDown('ctrl')
        pg.keyDown(f'f8')
        pg.keyUp('ctrl')
        pg.keyUp(f'f8')
    if num == 9:
        pg.keyDown('ctrl')
        pg.keyDown(f'f9')
        pg.keyUp('ctrl')
        pg.keyUp(f'f9')
    elif num == 'v':
        pg.keyDown('ctrl')
        pg.keyDown('v')
        pg.keyUp('ctrl')
        pg.keyUp('v')
    elif num == 'n':
        pg.keyDown('ctrl')
        pg.keyDown('n')
        pg.keyUp('ctrl')
        pg.keyUp('n')
    elif num == '+':
        pg.keyDown('ctrl')
        pg.keyDown('num+')
        pg.keyUp('ctrl')
        pg.keyUp('num+')
    elif num == '-':
        pg.keyDown('ctrl')
        pg.keyDown('-')
        pg.keyUp('ctrl')
        pg.keyUp('-')
    elif num == 'c':
        pg.keyDown('ctrl')
        pg.keyDown('c')
        pg.keyUp('ctrl')
        pg.keyUp('c')
    elif num == 'p':
        pg.keyDown('ctrl')
        pg.keyDown('p')
        pg.keyUp('ctrl')
        pg.keyUp('p')
    elif num == 'k':
        pg.keyDown('ctrl')
        pg.keyDown('k')
        pg.keyUp('ctrl')
        pg.keyUp('k')
    elif num == 'e':
        pg.keyDown('ctrl')
        pg.keyDown('e')
        pg.keyUp('ctrl')
        pg.keyUp('e')
    elif num == 'r':
        pg.keyDown('ctrl')
        pg.keyDown('r')
        pg.keyUp('ctrl')
        pg.keyUp('r')
    elif num == 0:
        pg.keyDown('shift')
        pg.keyDown('f10')
        pg.keyUp('shift')
        pg.keyUp('f10')
    


ser = serial.Serial(


    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
            timeout=0
)


print(f'Connected to: {ser.portstr}')

byte = input(b'> ')




line = []
while True:
    ser.write(byte.encode())
    for line in ser.read():
        print(str('Pressed Key : ') + chr(line))
        if chr(line) == '1':
            print('pressed')
            enterKey(1)
        if chr(line) == '2':
            print('pressed')
            enterKey(2)
        if chr(line) == '3':
            print('pressed')
            enterKey(3)
        if chr(line) == '4':
            print('pressed')
            enterKey(4)
        if chr(line) == '5':
            print('pressed')
            enterKey(5)
        if chr(line) == '6':
            print('pressed')
            enterKey(6)
        if chr(line) == '7':
            print('pressed')
            enterKey(7)
        if chr(line) == '8':
            print('pressed')
            enterKey(8)
        if chr(line) == '9':
            print('pressed')
            enterKey(9)
        if chr(line) == '0':
            print('pressed')
            enterKey(0)
        if chr(line) == 'v':
            print('pressed')
            enterKey('v')
        if chr(line) == 'n':
            print('pressed')
            enterKey('n')
        if chr(line) == 'c':
            print('pressed')
            enterKey('c')
        if chr(line) == 'p':
            print('pressed')
            enterKey('p')
        if chr(line) == 'r':
            print('pressed')
            enterKey('r')
        if chr(line) == 'e':
            print('pressed')
            enterKey('e')
        if chr(line) == 'k':
            print('pressed')
            enterKey('k')


ser.close()