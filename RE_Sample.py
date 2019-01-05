#!/usr/bin/python3
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

phone = "2004-959-559 # This is Phone Number"

num = re.sub(r'#.*$',"Radhakrishnan",phone)
print(num)

num = re.sub(r'\D',"",phone)
print(num)
