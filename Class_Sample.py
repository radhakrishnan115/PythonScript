class Employee:
    def __init__(self, regId, name):
        self.regId = regId
        self.name = name
    def getRegId(self):
        return self.regId
    def setRegId(self1,regId):
        self1.regId = regId
    def dipslayValue(self):
        print("Hello, Thanks for calling")

class Student(Employee):
    regId = 0
    name = ""
    address = ""
    def __init__(self,regId,name):
        self.regId = regId
        self.name = name

Obj1 = Student(115,"Radhakrishnan")
print(Obj1.__dict__)
print(Obj1.dipslayValue())
