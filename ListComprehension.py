a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
finList = []
length = len(a)
i = 0
while i < length:
    if i%2 != 0:
        finList.append(a[i])
    i+=1
print("Comprehensions list are - ", finList)
