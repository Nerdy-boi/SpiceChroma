from spiceapi import lights, connection
import array
from ChromaPython import ChromaDevices
import time


Actconnect = connection.Connection("localhost",5000,"1234")
active = True
while active == True:
  RawInput = lights.lights_read(Actconnect)
  Play1Raw = [RawInput[0][1], RawInput[1][1], RawInput[2][1], RawInput[3][1], RawInput[4][1], RawInput[5][1], RawInput[7][1], RawInput[14][1], RawInput[16][1], RawInput[17][1]]
  keyarr = ['z', 's', 'x', 'd', 'c', 'f', 'v', 'q', 'w', 'e']
  xarr = [4,4,5,5,6,6,7,3,4,5]
  yarr = [5,4,5,4,5,4,5,3,3,3]
  i=1
  for x in Play1Raw:
    for y in Play1Raw:
      if Play1Raw[i] < 0.5:
        ButtonUpdate(xarr[i], yarr[i], 0, 0, 0)
        time.sleep(0.16)
      else:
        ButtonUpdate(xarr[i], yarr[i], 255, 255, 255)
        time.sleep(0.16)






def ButtonUpdate (x, y, hexc):
  ChromaDevices.Keyboard.setPosition(hexc, x, y)

