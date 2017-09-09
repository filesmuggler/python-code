import time, os, sys,transpositionDecrypt,detectHumLang

def main():
    print(">> BRUTE FORCE TRANSPOSITON CIPHER FILE DECRYPTION PROGRAM <<")
    print("Write the name of the file you want to decrypt: ")
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
    
    outputFileName = 'decrypted-file.txt'

    if(os.path.exists(outputFileName)):
        print("Previous decrypted file exists. Do you want to overwrite it? (Y)es/(N)o")
        response = input("> ")
        if not response.lower().startswith('y'):
            while(os.path.exists(outputFileName)):
                outputFileName=input('Please give a new name > ')
    
    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close()

    print('decrypting is on...')

    startTime = time.time()
    outputFileObj = open(outputFileName,'w')

    for key in range(1,len(content)):
        translated = transpositionDecrypt.decryptMessage(key,content)
        is_english = detectHumLang.isEnglish(translated,80,80)
        if(is_english):
            print("Key: %s; Message: %s"%(key,translated[0:40]))
            outputFileObj.write("Key: %s"%(key))
            outputFileObj.write(translated)
            outputFileObj.write('\n\n\n')
            
    outputFileObj.close()
    totalTime = round(time.time()-startTime,2)
    print("Decrypting time: %s seconds"%(totalTime))

if __name__=='__main__':
     main()

   
    

