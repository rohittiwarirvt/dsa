
string = "xyz"
key = 2

def caesarCipherEncryptor(string, key):
  offset = key %26
  result = []
  alphabets = list("abcdefghijklmnopqrstuvwxyz")
  for letter in string:
    char = getNextCharacter(alphabets, letter, offset)
    result.append(char)

  return "".join(result)

def getNextCharacter(alphabets, letter, offset):
  newLetterCode = alphabets.index(letter) + offset
  return alphabets[newLetterCode % 26]



def caesarCipherEncryptorS2(string, key):
  pass

print(caesarCipherEncryptor(string, key))