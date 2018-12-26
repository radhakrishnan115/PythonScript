print("krishnan")
list1 = {"planId" : "T18001042",
         "impId"  : "T18001042_001",
         "developerName" : "Radhakrishnan"}
list1[1] = 'Street Name'

print(list1[1])
del list1[1]
print(list1)
list1.clear()
print('After Clearing', list1)
list1['hi'] = 'Radhakrishnan back'
print(list1['hi'])

