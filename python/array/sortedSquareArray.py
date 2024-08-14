
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

array = [1,2,-3,5,6,8,-9]
array = [-5, -4, -3, -2, -1]
# output = [1,4,9,25,36,64,81]

# O(nlogn) Time | O(n) Space
def sortedSquareArrayS1(array):
   list = [ num*num for num in array]
   list.sort()
   return list


# O(n) time | O(n) space - where n is the length of the input array
def sortedSquareArrayS2(array):
  result = [0 for _ in array]
  leftIdx = 0
  rightIdx = len(array) -1

  for idx in reversed(range(len(array))):
    smallerValue = array[leftIdx]
    largerValue = array[rightIdx]

    if abs(smallerValue) > abs(largerValue):
      result[idx] = smallerValue*smallerValue
      leftIdx+=1
    else:
      result[idx] = largerValue*largerValue
      rightIdx-=1
  return result



print(sortedSquareArrayS2(array))