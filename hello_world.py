for x in range(8):
   if(x%2 == 0):
      Colm1 = 'BLACK'
      Colm2 = 'WHITE'
   else:
      Colm1 = 'WHITE'
      Colm2 = 'BLACK'
   for j in range(8):
      if(j%2 == 0):
         print(Colm1,end='|')
      else:
         print(Colm2,end='|')
   print('\n')
print("End of Program")


