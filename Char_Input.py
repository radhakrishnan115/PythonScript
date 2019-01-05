name = input("Your Good Name")
DOB = input("Age please in DD/MM/YYYY")
n = input("Tell me how many times you want me to print your name")
age = DOB.split("/")
print("Your age at 100 years later", int(age[2])+100)
name+="\n"
print(name*int(n))
