def letterCounter(sentence):
  letterDict = {}
  for i in range(len(sentence)):
    if (sentence[i] in letterDict):
      letterDict[sentence[i]] += 1
    else:
      letterDict[sentence[i]] = 1

  orderedLetterDict = dict(sorted(letterDict.items()))

  return orderedLetterDict


def Main():
  sentence = "AaBbCc"

  letterCount = letterCounter(sentence)

  for i in letterCount:
    print(i, " ", letterCount[i])

Main()
