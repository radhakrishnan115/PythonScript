a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fList = []
for n in a:
    if n < 10:
        fList.append(n)
#print("List of Numbers less than 10 are - " , fList)

inputNum = int(input("Enter the Number "))
if inputNum in a:
    print("Whoooo Great!!! Entered number ", inputNum, " is available in my list")
else:
    print("OOOPS!!! I am Sorry")

