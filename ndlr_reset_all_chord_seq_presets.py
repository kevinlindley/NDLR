#
#  Author      : Kevin Lindley
#  Date        : 2023-12-17
#  Version     : 1.1.0
#  Filename    : ndlr_reset_all_chord_seq_presets.py
#  Description : Resets all of the NDLR's Chord Sequencers to Empty.
#

import serial
import time
import sys

#Change the Serial Port to the one used by your system in the variable below.
#
COM_PORT = "COM7"

# Connect to your Serial Port.
try:
    serialPort = serial.Serial(port=COM_PORT, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except Exception as e:
    print ("Error Opening serial port: " + COM_PORT + "  Try editing the COM_PORT value on line 14")
    sys.exit(1)

if serialPort.isOpen():
    print ("Zeroing NDLR's Chord Sequences 1-5")
    serialPort.flushInput()
    serialPort.flushOutput()
    # For each Chord Sequence Preset 1 to 5.
    #
    for chord_sequence_preset_num in ["1","2","3","4","5"]:
        outputstring = "<CSeq" + chord_sequence_preset_num + "-" + "0," * 105 + "0>\r\n"
        print("Reset " + chord_sequence_preset_num + " : ",end="")
        serialPort.write(outputstring.encode('ascii')) 
        time.sleep(0.1)
        numberOfLine = 0
        while True:
            response = serialPort.readline().decode('ascii')
            print(response[:-3])
            numberOfLine = numberOfLine + 1
            if (numberOfLine >= 1):
               break
    serialPort.close()
else:
    print ("Cannot open serial port.")
