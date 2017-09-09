 ## http://inventwithpython.com/hacking (BSD Licensed) 
 ## Krzysztof Stężała (BSD License)

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    print("Write the name of the file you want to encrypt or decrypt: ")
    inputFileName = input('> ')

    fileExist = os.path.exists(inputFileName)
    while not fileExist:
        print('The file %s does not exist. Quitting...' % (inputFileName))
        print('Do you want to try again? (C)ontiue or (Q)uit')
        inputFileName = input('> ')
        fileExist = os.path.exists(inputFileName)
        if not inputFileName.lower().startswith('c'):
            print('Quiting program...')
            sys.exit()

    print('Do you want to (E)ncrypt or (D)ecrypt the file content?')
    myMode = input('> ')   

    if myMode.lower().startswith('e'):
        myMode = 'encrypt'
    elif myMode.lower().startswith('d'):
        myMode = 'decrypt'

    myKey = 10
    
    outputFileName = 'frankenstein-'+myMode+'ed.txt'

    if os.path.exists(outputFileName):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?'%(outputFileName))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close()

    print('%sing...'%(myMode.title()))

    startTime = time.time()

    if myMode == "encrypt":
        translated = transpositionEncrypt.encryptMessage(myKey,content)
    elif myMode == "decrypt":
        translated = transpositionDecrypt.decryptMessage(myKey,content)
    
    totalTime = round(time.time()-startTime,2)
    print("%sion time: %s seconds" % (myMode.title(),totalTime))

    outputFileObj = open(outputFileName,'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode,inputFileName,len(content)))
    print('%sed file is %s.' % (myMode.title(),outputFileName))


## invoke main() function at startup of the script or module
if __name__=='__main__':
    main()


