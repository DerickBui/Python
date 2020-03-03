class Person:
    person_count = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        #Person.person_count += 1;

    def info(self):
        print("This person's first name is", self.first, "last name is", self.last)
