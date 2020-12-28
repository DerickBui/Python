def letterCounter(sentence):
  letterDict = {}
  for i in range(len(sentence)):
    if (sentence[i] in letterDict):
      letterDict[sentence[i]] += 1
    else:
      letterDict[sentence[i]] = 1

  orderedLetterDict = dict(sorted(letterDict.items()))

  return orderedLetterDict

def wordCounter(sentence):
  words = sentence.split()

  amount = len(words)

  return amount

def Main():
  sentence = "a a a a a. a"

  letterCount = letterCounter(sentence)

  for i in letterCount:
    print(i, " ", letterCount[i])

  print("Amount of words: ", wordCounter(sentence))

Main()
