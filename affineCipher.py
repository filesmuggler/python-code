import time, os, sys, cryptomath, random, printSetup, detectHumLang

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" #space is before exclamation mark

 

def main():
    #myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    myKey = 2023
    print("#############>> AFFINE CIPHER PROGRAM <<#############")
    print('\n')
    print("Write the name of the file you want to process: ")
    inputFileName = input("> ")

    fileExist = os.path.exists(inputFileName)
    
    while not fileExist:
        print("File named %s appears to not exist. Aborting... " % (inputFileName))
        print("Do you want to try again? (Y)es/(N)o")
        response_Abort = input("> ")
        if not response_Abort.lower().startswith('y'):
            print('Quitting program...')
            time.sleep(1)
            sys.exit()
        else:
            print("Provide the name of the file:")
            inputFileName = input("> ")
            fileExist = os.path.exists(inputFileName)

    inputFileObj = open(inputFileName)
    fileContent = inputFileObj.read()
    inputFileObj.close()

    print('Please select if to (E)ncrypt or (D)ecrypt the file:')
    response_Mode = input('> ')
    if response_Mode.lower().startswith('e'):
        myMode = 'encrypt'
    elif response_Mode.lower().startswith('d'):
        myMode = 'decrypt'
    else:
        print('Given bad mode. Aborting...')
        time.sleep(1)
        sys.exit()

    outputFileName = inputFileName

    if(os.path.exists(outputFileName)):
        print("Previous decrypted file exists. Do you want to overwrite? (Y)es/(N)o")
        response_FileOutput = input("> ")
        if not response_FileOutput.lower().startswith('y'):
            while(os.path.exists(outputFileName)):
                outputFileName = input("Please provide new name: > ")

    outputFileObj = open(outputFileName,"w")


    print("Started %sing %s file to %s..."%(myMode.title(),inputFileName.title(),outputFileName.title()))
    startTime = time.time()

    translated = processMessage(myMode,myKey,fileContent)

    outputFileObj.write(translated)
    outputFileObj.close()
    
    totalTime = round(time.time() - startTime,2)

    print("%sing time: %s seconds"%(myMode.title(),totalTime))

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS)-1:
        sys.exit('Key A must be greater then 0 and Key must be between 0 and %s.'%(len(SYMBOLS)-1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not reltively prime. Choose a different key.'%(keyA,len(SYMBOLS)))

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB    



def processMessage(mode,key,content):

    if mode == 'encrypt':
        keyA, keyB = getKeyParts(key)
        checkKeys(keyA,keyB,mode)
        ciphertext = ''
        for symbol in content:
            if symbol in SYMBOLS:
                #encrypt the symbol
                symIndex = SYMBOLS.find(symbol)
                ciphertext += SYMBOLS[(symIndex*keyA+keyB)%len(SYMBOLS)]

        return ciphertext

    elif mode == 'decrypt':
        keyA, keyB = getKeyParts(key)
        checkKeys(keyA,keyB,mode)
        plaintext=''
        modInverseOfKeyA = cryptomath.findModInverse(keyA,len(SYMBOLS))

        for symbol in content:
            if symbol in SYMBOLS:
                #decrypt the symbol
                symIndex = SYMBOLS.find(symbol)
                plaintext += SYMBOLS[(symIndex-keyB)*modInverseOfKeyA % len(SYMBOLS)]
            else:
                plaintext += symbol

        return plaintext

    else:
        sys.exit('Invalid mode applied! Quitting...')    

    



if __name__=="__main__":
    main()




