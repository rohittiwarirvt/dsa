
input_string = "AAAAAAAAAAAAABBCCCCDD"

# sample output = "9A4A2B4C2D"

def runLengthEncodingS1(input_string):

  encodingStringRes = []
  letterCount = 0
  for letIdx in range(1, len(input_string)):
    currentLetter = input_string[letIdx]
    prevLetter = input_string[letIdx -1]

    if currentLetter != prevLetter or letterCount == 9:
      encodingStringRes.append(str(letterCount))
      encodingStringRes.append(prevLetter)
      letterCount = 0
    letterCount +=1

  return "".join(encodingStringRes)


print(runLengthEncodingS1(input_string))