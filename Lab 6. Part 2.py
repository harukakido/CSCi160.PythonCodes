'''
Haruka Kido
haruka.kido@ndus.edu
ID: 1323392
CSci 160. Thurs 7-9PM.
Lab 6. Part 2: Read File Data and Display Relative Statistical Information  
'''

#file name request
import FileUtils
import os 

fileName = FileUtils.selectOpenFile ("Select data file")
if fileName == None:
      os._exit(0) 
      print ("Entered file doesn't exist.")
      
#if file exists, read all values in file
mode = 'r'
infile = open (fileName, 'r') #returns a "file handle"

line = ''
line.strip()
total = 0
count = 0
min = None
max = None

for line in infile:
      line = line.strip()
      print (line)
      total = total + int(line)
      count = count + 1
     
with open(fileName) as newfile:
    for line in newfile:
        num = int(line.strip())
        if min is None or num < min:
            min = num
        if max is None or num > max:
            max = num
            
print("The minimum value: " , min)     
print("The maximum value: " , max)       
print("The average: " , format(total/count, "5.3f"))      
print("The total number of values: " , count)

#add 70 into file for statistical outputs in comparison to 70
mode = 'w'
outFile = open(fileName, 'w') 
testscore = 0
while(testscore != -1 and 0 <= testscore <= 100): #establishes all numbers except -1 as loop condition
      testscore = int(input("Enter all test scores again (one by one). Include 70 as the comparative value, then type -1 to get statistical data: "))
      if testscore == -1:
            break
      else:
            outFile.write("%d\n" % testscore)   
outFile.close()

#makes file into list
#sorts list into sequential order
mode = 'r'
f = open(fileName,'r')
lines = [line.rstrip() for line in f]
intlines = list(map(int, lines))
intlines.sort()

#turns list into strings
makeitastring = ''.join(map(str, intlines))
name = makeitastring

seventy = name.find("70") 
closestbelow = name[0:seventy]
last_2_closestbelow = closestbelow[-2:]
print("The value closest to 70 WITHOUT going over 70: " , last_2_closestbelow)

s = name
seventy = s.find("70")
closest = s[0:seventy]
s = s[seventy + 1:]
s = s.strip()
first_three_closest = s[:3]
final_closest = first_three_closest[-2:]
print("The value closest to 70: " , final_closest)

outFile.close()     



      




