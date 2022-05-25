import time
import serial

def calculateChecksum(hexStr):
    total = 0
    for i in range(0, len(hexStr), 2):
        total += int(hexStr[i:i+2], 16)
    hexStr = hex(total)[-2:]
    return hexStr

ser = serial.Serial(
                port='/dev/serial0',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=.5
            )

time.sleep(2)

ser.flush()
ser.flushInput()

base_command = "55AA11"
switch_algorithm_command = base_command + "022D0400"
switch_algorithm_command += calculateChecksum(switch_algorithm_command)
ser.write(bytes.fromhex(switch_algorithm_command))

byteString = ser.read(5)
byteString += ser.read(int(byteString[3]))
byteString += ser.read(1)
print(byteString.hex())





