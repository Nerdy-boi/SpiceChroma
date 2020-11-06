from spiceapi import lights, connection
from array import *
#f = open("file.txt","w")
Actconnect = connection.Connection("localhost",5000,"1234")
#f.write(', '.join(map(str, lights_read(Actconnect))))

RawInput = lights.lights_read(Actconnect)

Play1 = [RawInput[0][1], RawInput[1][1], RawInput[2][1], RawInput[3][1], RawInput[4][1], RawInput[5][1], RawInput[7][1], RawInput[14][1], RawInput[16][1], RawInput[17][1]]
# 1, 2, 3, 4, 5, 6, 7, Start, VEFX, Effect