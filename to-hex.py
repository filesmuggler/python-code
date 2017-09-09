from decimal import *

def stringToHexadecimal(dataToConvert):
   
    convertedData = dataToConvert.hex()
    
    return(convertedData)

print(stringToHexadecimal("Hello"))