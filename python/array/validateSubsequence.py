

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
def isValidSubsequenceS1(array, sequence):
  seqIdx = 0
  arrIdx = 0
  while arrIdx < len(array) and seqIdx < len(sequence):
    if array[arrIdx] == sequence[seqIdx]:
      seqIdx+=1
    arrIdx+=1
  return seqIdx == len(sequence)

print(isValidSubsequenceS1(array, sequence))