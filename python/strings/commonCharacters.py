# https://leetcode.com/problems/find-common-characters/description/

strings = ["abc", "bcd", "cbaccd"]


# O(n*m) | O(c) where n is lethg or stirng and m is the longest character,
#  c is the unique characters across tring
def commonCharactersS1(strings):

  countCharacter = {}
  for string in strings:
    uniquecharacterString = set(string)
    for char in uniquecharacterString:
      if char not in countCharacter:
        countCharacter[char] =0
      countCharacter[char] +=1

  finalResult =[]
  for char, count in countCharacter.items():
    if count == len(strings):
      finalResult.append(char)

  return finalResult



def commonCharactersS2(strings):
  '''
   get the smallest string say potentialString
   run a loop compare potentialString with each string in strings
   for each character potentialString not current string , remove that character from
   potentialString

  '''

print(commonCharactersS1(strings))