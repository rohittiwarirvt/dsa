string = "abaxyzzyxf"

# sample output
# xyzzyx

# https://leetcode.com/problems/longest-palindromic-substring/description/
# O(n^3) time | O(n) space
def longestPalindromicSubstringS1(string):
  longestSbstr = ""
  for idx in range(len(string)):
    for jdx in range(idx, len(string)):
      substring = string[idx:jdx +1]
      if len(substring) > len(longestSbstr) and isPalindrome(substring):
        longestSbstr = substring

  return longestSbstr


def isPalindrome(string):
  leftIdx =0
  rightIdx = len(string) -1
  while leftIdx < rightIdx:
    if string[leftIdx] != string[rightIdx]:
      return False
    leftIdx+=1
    rightIdx-=1
  return True


# string = "abaxyzzyxf"


# O(n^2) | O(n) space
def longestPalindromicSubstringS2(string):
  currentLongest = [0,1]
  for idx in range(1, len(string)):
    odd = getLongestPalidromeFrom(string, idx-1, idx+1)
    even = getLongestPalidromeFrom(string, idx -1, idx)
    longest = max(odd, even, key=lambda x: x[1]-x[0])
    currentLongest = max(currentLongest, longest, key=lambda x:x[1] - x[0])
  return string[currentLongest[0]: currentLongest[1]]


def getLongestPalidromeFrom(string, leftIdx, rightIdx):
  while leftIdx >=0 and rightIdx < len(string):
    if string[leftIdx] != string[rightIdx]:
      break
    leftIdx-=1
    rightIdx+=1
  return [leftIdx + 1, rightIdx]

print(longestPalindromicSubstringS2(string))