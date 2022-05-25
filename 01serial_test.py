import time
import serial

ser = serial.Serial(
                port='/dev/serial0',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=.5
            )

time.sleep(2)

knock_command = "55AA11002C3C"
ser.write(bytes.fromhex(knock_command))

byteString = ser.read(5)
byteString += ser.read(int(byteString[3]))
byteString += ser.read(1)
print(byteString.hex())

