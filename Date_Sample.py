import time
import calendar
print('Current Date and Time ', time.asctime(time.localtime(time.time())))
print(calendar.month(2018,12))

def userFunc(arg1, *varName):
    "Function Demo Program"
    print(arg1)
    print("Hi", varName)

    for var in varName:
        print("Inside the for", var)

userFunc(10)
userFunc(10,12,13)
Radha = "Radha"
Krishnan = "Krishnan"
ravi = lambda Radha, Krishnan : Radha+Krishnan
print(ravi(Radha,Krishnan))
