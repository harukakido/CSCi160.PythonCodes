'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. Lab 02. Th 7-9PM
'''

#Part 3
#input 1: asks user to input number of credits earned to date
credits_to_date = int(input("Please enter the number of credits you have earned to date: "))

#input 2: asks user to input number of credits from this semester
credits_this_semester = int(input("Please enter the number of credits you are taking this semester: "))

#output 1: current class status based on completed credits
#freshman: 0-23 completed credits
if credits_to_date >= 0 and credits_to_date <= 23:
   print ("Current class status: freshman")

#sophomore: 24-59 completed credits
if credits_to_date >= 24 and credits_to_date <= 59:
   print ("Current class status: sophomore")
   
#junior: 60-89 completed credits
if credits_to_date >= 60 and credits_to_date <= 89:
   print ("Current class status: junior")
   
#senior: 90 or more completed credits
if credits_to_date >= 90:
   print ("Current class status: senior")

#output 2: anticipated class status following the current semester
total_credits_following_current_semester = credits_to_date + credits_this_semester

#freshman: 0-23 completed credits
if total_credits_following_current_semester >= 0 and total_credits_following_current_semester <= 23:
   print ("Anticipated class status following the current semester: freshman")

#sophomore: 24-59 completed credits
if total_credits_following_current_semester >= 24 and total_credits_following_current_semester <= 59:
   print ("Anticipated class status following the current semester: sophomore")
   
#junior: 60-89 completed credits
if total_credits_following_current_semester >= 60 and total_credits_following_current_semester <= 89:
   print ("Anticipated class status following the current semester: junior")
   
#senior: 90 or more completed credits
if total_credits_following_current_semester >= 90:
   print ("Anticipated class status following the current semester: senior")

#output 3: minimum number of additional credits needed to graduate after this semester
#120 credits needed to graduate from UND
min_additional_credits_to_graduate = 120 - total_credits_following_current_semester
print ("Minimum number of additional credits needed to graduate after this semester:" , min_additional_credits_to_graduate)

#output 4: number of additional semesters it will take to graduate if 15 credits taken per semester
#assuming passing grade for every course
num_of_additional_semesters_it_will_take_to_graduate = min_additional_credits_to_graduate / 15

if num_of_additional_semesters_it_will_take_to_graduate <= 1:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 1")
   
if num_of_additional_semesters_it_will_take_to_graduate > 1 and num_of_additional_semesters_it_will_take_to_graduate <= 2:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 2")
   
if num_of_additional_semesters_it_will_take_to_graduate > 2 and num_of_additional_semesters_it_will_take_to_graduate <= 3:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 3")
   
if num_of_additional_semesters_it_will_take_to_graduate > 3 and num_of_additional_semesters_it_will_take_to_graduate <= 4:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 4")
   
if num_of_additional_semesters_it_will_take_to_graduate > 4 and num_of_additional_semesters_it_will_take_to_graduate <= 5:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 5")
      
if num_of_additional_semesters_it_will_take_to_graduate > 5 and num_of_additional_semesters_it_will_take_to_graduate <= 6:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 6")
      
if num_of_additional_semesters_it_will_take_to_graduate > 6 and num_of_additional_semesters_it_will_take_to_graduate <= 7:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 7")
         
if num_of_additional_semesters_it_will_take_to_graduate > 7 and num_of_additional_semesters_it_will_take_to_graduate <= 8:
   print ("Number of additional semesters it will take to graduate if 15 credits taken per semester: 8")
      

