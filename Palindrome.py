inputStr = input('Enter your Name to check the palindrome')
lenStr = len(inputStr)
i = 0
j = lenStr-1
while i < lenStr:
    if inputStr[i] != inputStr[j]:
        print("Given Name is not palindrome ", inputStr)
        break
    i+=1
    j-=1
if i == lenStr:
    print("Great, Entered name is palindrome ", inputStr)


