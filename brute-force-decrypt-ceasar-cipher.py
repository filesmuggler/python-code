import detectHumLang


with open("secret-message.txt", "r") as myFile:
    dataFromFile = myFile.read().replace('\n',' ')

myFile.close()

key = 0

myset = 'abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPRQSTUWVXYZ0123456789'

while (key <= len(myset)):
    decryptedMessage = ''
    #decrypt message
    for symbol in dataFromFile:
        if symbol in myset:
            num = myset.find(symbol)
            num = num - key
            if (num > len(myset)):
                num = num - len(myset)
            elif (num < 0):
                num = num + len(myset)
            
            decryptedMessage = decryptedMessage + myset[num]
        else:
            decryptedMessage = decryptedMessage + symbol

        
    is_english = detectHumLang.isEnglish(decryptedMessage)
    if(is_english):
        decryptedMessage = 'key: ' + str(key) + '; message: ' + decryptedMessage        
        print(decryptedMessage)
    
    #increment key and start again
    key = key + 1
    
