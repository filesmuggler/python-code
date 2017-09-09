 ## http://inventwithpython.com/hacking (BSD Licensed) 
 ## Krzysztof Stężała (BSD License)

import math,sys,time

##   main() is the main function of this script or module.
def main():
    # encrypted message and key
    myMessage = 'Rg r!ahb itecnssoy td a inrfnieog'
    myKey = 8

    # getting original message
    plaintext = decryptMessage(myKey,myMessage)

    print('Key: '+str(myKey)+'; Plain Text: '+plaintext + '|')

##   function to decrypt messages ciphered with transposition method
##   it puts single characters from encrypted message into matrix of boxes
##   which is "message length/key wide" and "key high"
def decryptMessage(key,message):
    # displaying loading 
    for i in range(4):
        b="Decrypting with key: " + str(key) + "."*i
        print(b,end="\r")
        time.sleep(0.2)

    print("                                                            ",end='\r')
    time.sleep(0.1)
    # number of columns rounded up to upper bound (how long is the list of strings)
    numOfColumns = math.ceil(len(message)/key)
    # number of rows (how long is the string in the list of strings)
    numOfRows = key
    # determining how many 'boxes' should remain empty ever after
    numOfShadedBoxes = (numOfColumns*numOfRows)-len(message)

    # creating list with empty strings
    plaintext = ['']*numOfColumns

    # initial setup
    col = 0
    row = 0

    # main algorithm for decrypting the message
    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if(col==numOfColumns) or (col == numOfColumns-1 and row >=numOfRows-numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()