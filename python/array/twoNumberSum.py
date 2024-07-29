
## two number sum
# https://leetcode.com/problems/two-sum/description/

# brute force

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
# O(n^2) time | O(1) space
def twoNumberSums1(array, targetSum):
  for i in range(len(array)):
    firstNum = array[i]
    for j in range(i +1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]
  return []


# O(n) time | O(n)
def twoNumberSums2(array, targetSum):
  nums = {}
  for firstNum in array:
    potentialMatch = targetSum - firstNum
    if potentialMatch in nums:
      return [potentialMatch, firstNum]
    else:
      nums[firstNum] = True
  return  []

print(twoNumberSums2(array, targetSum))

# O(nlogn) | O(1) space
def twoNumberSums3(array, targetSum):
  array.sort()
  left = 0;
  right = len(array) -1
  while left < right:
    currentSum = array[left] + array[right]
    if currentSum < targetSum:
      left+=1
    elif currentSum > targetSum:
      right-=1
    elif currentSum == targetSum:
      return [array[left], array[right]]
  return []
