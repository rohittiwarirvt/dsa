
string = "abcdcaf"
#Sample output
#1

def firstNonRepeatingCharacterS1(string):
 for idx in range(len(string)):
   isRepeating = False
   for jdx in range(len(string)):
      if idx != jdx  and string[idx] == string[jdx]:
         isRepeating = True
   if not isRepeating:
      return string[idx]


# O(n) time | O(n) space
def firstNonRepeatingCharacterS2(string):
  characterFrequency = {}
  for character in string:
    characterFrequency[character] = characterFrequency.get(character, 0) + 1

  for character in string:
    if characterFrequency[character] == 1:
      return character

  return -1

print(firstNonRepeatingCharacterS2(string))