fileName = input("Input the file name: ")
from os import path
from time import sleep
import sys

def convertIntoByteUnits(value):
    units = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    result = ""
    for i in range(1, len(units) + 1):
        if (value % 1024 != 0):
            result = str(value % 1024) + " " + units[i - 1] + " " + result
        value = int(value / 1024)
    return result + "                 "

print()
while (True):
    print ("Size: {}".format(convertIntoByteUnits(path.getsize(fileName))), end="\r", flush=True)
    sleep(0.005)
