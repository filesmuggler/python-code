### Detect Human Language words module
### BSD license by Krzysztof Stężała
### 
### to use the module
### import detectHumLang
### detecteHumLang.isEnglish() returns True or False if english
### 

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUWYXZ'
LETTERS_AND_SPACES = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('english-dict.txt')
    englishWords = {}
    for word in dictionaryFile.read().upper().split('\n'):
        englishWords[word]=None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACES:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches)/len(possibleWords)



def isEnglish(message,wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message)*100 >=wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters)/len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch