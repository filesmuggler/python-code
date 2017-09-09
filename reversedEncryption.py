# Reverse string encryption

message = input('Enter the message: ')

i = len(message) - 1

translated = ''

while (i>=0):
    translated = translated + message[i]
    i = i - 1

print(translated)