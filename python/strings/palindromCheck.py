
string = "abcdcba"


#O(n^2) time | O(n) space insertion is n2
def isPalindromeS1(string):
  reversedString =""
  for i in reversed(range(len(string))):
    reversedString += string[i]
  return string == reversedString

#O(n) time | O(n) space
def isPalindromeS2(string):
  reversedChars = []
  for i in reversed(range(len(string))):
    reversedChars.append(string[i])
  return string == "".join(reversedChars)

# O(n) time | O(n) space
def isPalindromeS3(string, i=0):
  j = len(string) -1 -i
  True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)


# O(n) time | O(n) space
def isPalindromeS4(string):
  leftIdx = 0
  rightIdx = len(string) -1

  while (left < rightIdx):
    if string[leftIdx] != string[rightIdx]:
      return False
    leftIdx+=1
    rightIdx-=1

print(isPalindromeS1(string))