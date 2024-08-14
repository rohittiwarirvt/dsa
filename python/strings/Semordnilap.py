
words = ["dog", "desserts", "god", "stressed", "aaa", "bbbb", "racecar"]

def semordnilap(words):
  wordSet = set(words)
  result = []
  for word in words:
    reversedWord = word[::-1]
    if reversedWord in wordSet and word != reversedWord:
      result.append([word, reversedWord])
      wordSet.remove(reversedWord)
      wordSet.remove(word)
  return result


print(semordnilap(words))