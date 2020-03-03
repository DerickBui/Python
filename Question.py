import random
class Question:
    totalCorrect = 0
    #number1 = 0
    #number2 = 0
    #correctAns = 0

    def __init__(self):
        self.number1 = random.randrange(0, 50)
        self.number2 = random.randrange(0, 50)
        self.correctAns = self.number1 + self.number2

    def answering(self):
        print(self.number1, " + ", self.number2)
        answer = input();
        if int(answer) == self.correctAns:
            print("Correct")
            print(self.correctAns);
        else:
            print("Wrong")
            print(self.correctAns)