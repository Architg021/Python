class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.company) '''now this will cause ambiguity bcz now which company it will print visa or fiver it will print fiver here bcz 
we have written freelance first in this programmer class if had writeen employee first visa would have been printed so the class which is written
first it will acquire all those properties and variables of it that is multiple inheritance'''
