message = input('Enter message: ')
key = input('Enter key: ')
key = int(key)

LETTERS = 'abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPRQSTUWVXYZ0123456789'

translated = ''



for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = num + key
      
        if num > len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol

file = open("secret-message.txt","w")
file.write(translated)
file.close()
print(translated)
    
 
