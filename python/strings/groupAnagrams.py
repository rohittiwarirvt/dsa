
words =  ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]


# O(w*nlog(n) + n*w*log(w) time | O(wn) space - where w is the number of words and
# n is the slenght oth longest word
def groupAnagramsS1(words):
  sortedWords = ["".join(sorted(word)) for word in words]
  indices = [idx for idx in range(len(words))]
  indices.sort(key=lambda x: sortedWords[x])
  print(words)
  print(sortedWords)
  print(indices)
  result = []
  currentAnagram = sortedWords[indices[0]]
  currentAnagramGroup = []
  for index in indices:
    word = words[index]
    sortedWord = sortedWords[index]

    if currentAnagram == sortedWord:
      currentAnagramGroup.append(word)
      continue
    result.append(currentAnagramGroup)
    currentAnagram = sortedWord
    currentAnagramGroup = [word]

  result.append(currentAnagramGroup)
  return result

#  [oy, act, flop, act, foo, act, oy, flop]
# [
#   ["foo"],
#   ["flop", "olfp"],
#   ["oy", "yo"],
#   ["act", "cat", "tac"]
# ]


def groupAnagramsS2(words):
  anagramHashMap = {}

  for word in words:
    sortedWord = "".join(sorted(word))
    if sortedWord in anagramHashMap:
      anagramHashMap[sortedWord].append(word)
    else:
      anagramHashMap[sortedWord] = [word]

  return list(anagramHashMap.values())

print(groupAnagramsS2(words))

#  1, 3, 5, 2,7, 0, 6,


