#
#  Author      : Kevin Lindley
#  Date        : 2023-12-19
#  Version     : 1.1.0
#  Filename    : NDLRpget.py
#  Description : Retrives the NDLR patterns 21 to 40 and outputs them 
#  Usage       : python NDRpget.py > NewPattFile.txt
#
#
import serial
import time
import sys
#
#Change the Serial Port to the one used by your system in the variable below.
#
COM_PORT = "COM7"
#
# Connect to your Serial Port.
try:
    serialPort = serial.Serial(port=COM_PORT, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except Exception as e:
    print ("Error Opening serial port: " + COM_PORT + "  Try editing the COM_PORT value on line 14")
    sys.exit(1)
#
lines = ""
#
if serialPort.isOpen():
    serialPort.flushInput()
    serialPort.flushOutput()
    outputstring = "d\r\n"
    serialPort.write(outputstring.encode('ascii')) 
    time.sleep(0.25)
    numberOfLine = 0
    while True:
        response = serialPort.readline().decode('ascii')
        if (numberOfLine > 1):
            pattern_split = response.split(" ")
            p_split=pattern_split[1]
            p_split = p_split[:-2]
            outputstring = "<Patt" + str(numberOfLine+20) + "-" + "20"+"," + p_split + ">"
            print(outputstring)
        numberOfLine = numberOfLine + 1
        lines += response
        if (numberOfLine > 21):
           break
    serialPort.close()
else:
    print ("Cannot open serial port.")

