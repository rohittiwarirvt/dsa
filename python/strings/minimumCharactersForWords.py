

words = ["this", "that", "did", "deed", "them!", "a"]

expectedOutput =["!", "a", "d", "d", "e", "e", "h", "i", "m", "s", "t", "t"]


def minimumCharactersForWords(words):
  maximumCharacterFrequency = {}
  for word in words:
    countCharFreq = countCharacterFrequencyInWord(word)
    updateMaximumCharacterFrequncy(countCharFreq, maximumCharacterFrequency)

  return createListfromCharacterFrequency(maximumCharacterFrequency)


def createListfromCharacterFrequency(listOfFrequecy):
  characters =[]
  for character in listOfFrequecy:
    frequency = listOfFrequecy[character]

    for _ in range(frequency):
      characters.append(character)

  characters.sort()

  return characters

def countCharacterFrequencyInWord(word):
  characterFrequency = {}
  for letter in word:
    if letter not in characterFrequency:
      characterFrequency[letter] =0
    characterFrequency[letter]+=1
  return characterFrequency


def updateMaximumCharacterFrequncy(characterFrequency, maximumCharacterFrequency):
  for character in characterFrequency:
    frequency = characterFrequency[character]

    if character in maximumCharacterFrequency:
      maximumCharacterFrequency[character] = max(frequency, maximumCharacterFrequency[character])
    else:
      maximumCharacterFrequency[character] = frequency



print(minimumCharactersForWords(words))