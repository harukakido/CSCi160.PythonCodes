'''
Haruka Kido
haruka.kido@ndus.edu
ID: 1323392
CSci 160. Thurs 7-9PM.
Weekly Lab 11. Dictionaries, Functions, Files  
'''

import os

def readData(fileName):
   data = { }
   if not fileName.endswith('.txt'):
             fileName += '.txt'             
   file = open(fileName).read().split('\n') #lines to list conversion
   while "" in file: file.remove("") #empty lines extracted out
   for lines in file:
      name,date = lines.split(":")
      data[int(date)] = name #adds data into dictionary
   if fileName == None:
      os._exit(0) 
      print ("Entered file doesn't exist.")  
   return data

def insertName():
   name = input("Enter the name to add: ")
   date = int(input("Enter the date associated with name: "))
   if date in dictionary: #if date is already in dictionary
       print("Date is already taken by '%s'"%dictionary[date])
   else: #if valid name, add name as a new value to dictionary
       dictionary[date] = name #associates date as value to name as key

def searchDate():
   while True: #search date loop condition
       date = int(input("Enter the date to search: "))
       if date == 0: 
           break
       if date in dictionary: 
           print("The name is \"%s\""%dictionary[date]) 
       else:                 
           print("No name is associated with this date.")

def displayDates(): #displays dates
   birthdays = [ ]
   for name,date in dictionary.items():
       birthdays.append((name,date)) #turns dictionary into list for sequencing dates
   sequential = sorted(birthdays,key = lambda x: x[0])
   for name in sequential:
       print("{0:2} : {1}".format(name[0],name[1]))

def addSequentialDates(file):
   birthdays = []
   for name,date in dictionary.items():
       birthdays.append((name,date))
   sequential = sorted(birthdays,key = lambda x: x[0])
   newfile = open(file,'w')
   for name in sequential:
      newfile.write("%s:%s\n"%(name[1],name[0]))     
   
def showMenu(): 
   print("What would you like to do?")
   print("1. Open a data file")
   print("2. Add new name")
   print("3. Search by date")
   print("4. Display all birthdays for the month")
   print("5. Exit program")
   print()   

showMenu()

dictionary = { }
fileName = " "

while True:
   userInput = int(input("Your choice? [Type in the number as the choice]: "))
   if userInput == 1:
      fileName = input("Enter the file name: ")
      dictionary = readData(fileName)
   elif userInput == 2:
      insertName()
   elif userInput == 3:
      searchDate()
   elif userInput == 4:
      displayDates()
   elif userInput == 5:
      addSequentialDates(fileName)
      exit()
      outFile.close()
   else:
      print("Input unidentified.")
       
