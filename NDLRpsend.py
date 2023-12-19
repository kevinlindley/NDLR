#
#  Author      : Kevin Lindley
#  Date        : 2023-12-19
#  Version     : 1.1.0
#  Filename    : NDLRpsend.py
#  Description : Send a patterns from stdin to the NDLR's COM port
#  Usage       : python NDLRpsend.py < NDLR_Patt_Blank.txt
#
#
import sys
import serial
#
# Change the Serial Port to the one used by your system in the variable below:
#
COM_PORT = "COM7"
# NDLR_ba = bytearray()
#
# Connect to the Serial Port
#
print("Sending Patterns file to NDLR [",end="")
serialPort = serial.Serial(port=COM_PORT, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
for line in sys.stdin:
    print(".",end="")
    # NDLR_ba.extend(map(ord, line))
    # serialPort.write(NDLR_ba)
    serialPort.write(line.encode('ascii')) 
print("] Done")
#
# Disconnect
#
serialPort.close()
#
