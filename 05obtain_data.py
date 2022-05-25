from huskylib import HuskyLensLibrary
import time 
import json

hl = HuskyLensLibrary("SERIAL", "/dev/serial0",9600)

hl.algorthim( "ALGORITHM_COLOR_RECOGNITION")

def printObjectNicely(obj):
    count=1
    if(type(obj)==list):
        for i in obj:
            print("\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__))
            count+=1
    else:
        print("\t "+ ("BLOCK_" if obj.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(obj.__dict__))


while True:
    printObjectNicely(hl.requestAll())
    time.sleep(1)

