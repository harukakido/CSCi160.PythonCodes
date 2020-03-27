'''
Haruka Kido
haruka.kido@ndus.edu
CSci 160. Weekly Lab 8 Part 2 
Working with lists, functions, and files
Thurs 7-9 PM
'''

#largest value
def largest(scores):
      max_s = scores[0]
      for s in scores:
            if s > max_s:
                  max_s = s

      return max_s

#smallest value
def smallest(scores):
      min_s = scores[0]
      for s in scores:
            if s < min_s:
                  min_s = s

      return min_s

#average value
def average(scores):
      sum = 0
      for s in scores:
            sum += s

      return sum / len(scores)

#match for numbers contained within upper and lower limits
def matching(scores, upper, lower):
      match = []
      for s in scores:
            if lower <= s <= upper:
                  match.append(s)

      return match


#main
if __name__ == '__main__':
      while True:
            print("Enter existing file name: " , end = '')
            fileName = input()

            #secures files as .txt
            if not fileName.endswith('.txt'):
                  fileName += '.txt'

            #secures file existence
            try:
                  file = open(fileName , 'r')
            except FileNotFoundError:
                  print("File does not exist.")
                  continue

            #converts data into values in a list
            data = file.readlines()
            scores = [int(line.strip()) for line in data]

            file.close()

            #print statements' string alignments
            format_string = '{rightscores1:>4}'
            format_string2 = '{rightscores2:>3}'
           
            print("Largest score: " , format_string.format(rightscores1 = (largest(scores))))
            print("Smallest score: " , format_string2.format(rightscores2 = (smallest(scores))))
            print("Average score: {0:.2f}".format(average(scores)))
            
            print()
            
            print("Searching for values:")
            print("Enter upper limit: " , end = '')
            upper = int(input())
            print("Enter lower limit: " , end = '')
            lower = int(input())
            
            print("Matching values: " , *matching(scores, upper, lower))
            
            print("Enter y to input new existing file or n to end program entirely: ", end = '')
            newFile = input()
            if newFile.lower() == 'n':
                  break