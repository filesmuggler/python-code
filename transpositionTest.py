 ## http://inventwithpython.com/hacking (BSD Licensed) 
 ## Krzysztof Stężała (BSD License)

import random,sys,transpositionEncrypt,transpositionDecrypt

#   main() is the main function of this script or module.
#   main() executes testing for encryption and decryption programs
#   from modules transpositionEncrypt and transpositionDecrypt.
def main():
    # static random number
    random.seed(42)

    # main loop for testing 
    # range(128) means 128 checks
    for i in range(128):
        # creating string that has the lenght of 'ABC...' multiplied by
        # a random number from 4 to 200
        message = 'ABCDEFGHIJKLMNOPQRSTUWXYZ1234567890' * random.randint(4,200)

        # converting string to list
        message = list(message)
        # generating random message from list
        random.shuffle(message)
        # back to string
        message = ''.join(message)

        # printing test number and data
        print('Test #%s: "%s..."'%(i+1,message[:40]))

        # check all possible keys for each message
        for key in range(1,len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key,message)
            decrypted = transpositionDecrypt.decryptMessage(key,encrypted)

            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key,message))
                print(decrypted)
                sys.exit()
    print('Transportation cipher test passed.')

if __name__ == "__main__":
    main()