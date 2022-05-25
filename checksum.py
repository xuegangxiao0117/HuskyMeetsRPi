def calculateChecksum(hexStr):
    total = 0
    for i in range(0, len(hexStr), 2):
        total += int(hexStr[i:i+2], 16)
    hexStr = hex(total)[-2:]
    return hexStr

print(calculateChecksum("55AA11"+"022D0100"))