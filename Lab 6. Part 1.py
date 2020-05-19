'''
Haruka Kido
haruka.kido@ndus.edu
ID: 1323392
CSci 160. Thurs 7-9PM.
Lab 6. Part 1: File Test Score Input  
'''

import FileUtils
import os

#file name request
fileName = 'numbers1.txt'
fileName = FileUtils.selectOpenFile ("Select data file")
if fileName == None: 
      print ("Entered file doesn't exist.")
      os._exit(0) 

#write information into same file
mode = 'w'
outFile = open(fileName, 'w') 
testscore = 0
while(testscore != -1 and 0 <= testscore <= 100): #establishes all numbers except -1 as loop condition
      testscore = int(input("Enter a test score 0-100 and -1 to quit: "))
      if testscore == -1:
            break
      elif testscore < 0 or testscore > 100:
            print("Test score must be between 0 to 100. Enter test score number between 0 to 100: ")
      else:
            outFile.write("%d\n" % testscore)     
            
outFile.close()
