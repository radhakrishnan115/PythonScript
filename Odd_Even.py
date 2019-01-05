num = input('Enter the Number')
num = int(num)
if num%2 == 0 and num%4 == 0:
    print("Hey Great, Enter number is multipe of 4 ")
elif num%2 == 0:
    print("Hey great, enter number", num , " is Even Number")
else:
    print("Hey Great, entered number ", num, " is odd")
