
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

#(n + m ) time | O(c)  space - where n is the number of characters, m is
# the lengthof the document,  and c is the number of unique characters in
def generateDocumentS1(characters, document):
  characterCounts = {}
  for character in characters:
    if character not in characterCounts:
      characterCounts[character] = 0
    characterCounts[character] +=1


  for documentLetter in document:
    if documentLetter not in characterCounts or characterCounts[documentLetter] == 0:
      return False
    characterCounts[document] =-1
  return True





def generateDocumentS2(characters, document):
  alreadyCounted = set()
  for letter in document:
    if letter in alreadyCounted:
      continue
    documentLetterCount = countCharacterFrequency(letter, document)
    characetLetterCount = countCharacterFrequency(letter, characters)
    if documentLetterCount > characetLetterCount:
      return False
    alreadyCounted.add(letter)
  return True


def countCharacterFrequency(letter, targetDocument):
  count = 0
  for alphabet in targetDocument:
    if letter == alphabet:
      count+=1
  return count




print(generateDocumentS1(characters, document))