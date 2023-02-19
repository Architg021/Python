class Employee:#base or parent class
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):#derived or child class
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")


e = Employee()#object of employee
e.showDetails()
p = Programmer()#object of programmer
p.showDetails()
p.getLanguage()
print(p.company)
