from huskylib import HuskyLensLibrary
import time 

hl = HuskyLensLibrary("SERIAL", "/dev/serial0",9600)

hl.algorthim( "ALGORITHM_COLOR_RECOGNITION")


while True:
    print(hl.requestAll())
    time.sleep(1)
