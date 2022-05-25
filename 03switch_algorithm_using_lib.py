from huskylib import HuskyLensLibrary
import time 
import json

hl = HuskyLensLibrary("SERIAL", "/dev/serial0",9600)

hl.algorthim( "ALGORITHM_COLOR_RECOGNITION")
