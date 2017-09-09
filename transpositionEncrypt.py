 ## http://inventwithpython.com/hacking (BSD Licensed) 
 ## Krzysztof Stężała (BSD License)

def main():
    myMessage = 'Rainy nights are best for coding!'
    myKey = 8    
    ciphertext = encryptMessage(myKey,myMessage)
    print('Key: '+str(myKey)+'; Ciphered Text: '+ciphertext + '|')
    

def encryptMessage(key,message):
    # ciphertext is array of empty strings multiplied by key
    # ciphertext = ['']*key == ciphertext = ['','','',...times (key-3)...]
    ciphertext = ['']*key

    # for every column in ciphertext array do the loop
    for col in range(key):
        #pointer lets follow the letters to be put in correct ciphertext array column
        pointer = col

        # do while pointer does not exceed the lenght of the message to collect all letters to correct columns
        while pointer<len(message):
            # writing correct letter to correct column
            ciphertext[col] += message[pointer]

            #moving pointer over
            pointer += key
        
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()