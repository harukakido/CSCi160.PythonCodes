'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. Lab 04. Th 7-9PM
'''

#Part A
#write individual while loops 
#print text before each loop to indicate parts 1-4
print ("Part 1")
#count from 10 to 50 (inclusive) by 1
#output 1 value per line
#initialize counter and target
counter = 10
endValue = 50
while counter <= endValue:
   print (counter)
   
   #update counter
   counter = counter + 1
   
print ()
print ("Part 2")
#count from 20 to 0 (inclusive, counting down)
#initialize counter and target
counter = 20
endValue = 0
while counter >= endValue:
   #all output on single line
   print (counter , end=' ')
   
   #update counter
   counter = counter - 1

print('\n')
print ("Part 3")
#count by 1/2 from 0 to 10 (inclusive)
#output 1 value per line
#initialize counter and target
counter = 0
endValue = 10
while counter <= endValue:
   print (counter)
      
   #update counter
   counter = counter + 1/2  
   
print ()
print ("Part 4")
#while loop
#ask for a single letter
letter = input("Enter a letter: ")

#set counter as lower case and set endValue as upper case
#initialize start counter
counter = 0

#initialize target
endValue = 0

#continue to ask for a single letter until the user enters the letter 'q' or 'Q' for quit
#do not echo the q back to the screen and do not count as an input
while(letter != 'Q' and letter != 'q'): #loop condition
    print("You entered " + "'" + str(letter) + "'")
    
    #lower case
    if(letter >= 'a' and letter <= 'z'):
        #counter increment
        counter += 1
    
    #upper case
    if (letter >= 'A' and letter <= 'Z'):
        #endValue increment 
        endValue += 1
        
    #loop continuation user input
    letter = input("Enter a letter: ")

#tells how many upper case and lower case letters were entered
#upper case count, not including Q or q
print()
print("The user entered" , endValue , "upper case letters")
#lower case count, not including Q or q
print("The user entered" , counter , "lower case letters")
