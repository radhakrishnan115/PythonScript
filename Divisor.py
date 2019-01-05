num = int(input("Enter the Number"))
numList = []
for a in range(1,16):
    if num %a == 0:
        numList.append(a)
print("Divisors are - ", numList)
