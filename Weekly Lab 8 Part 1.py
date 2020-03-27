'''
Haruka Kido
haruka.kido@ndus.edu
CSci 160. Weekly Lab 8 Part 1
Working with lists, functions, and files
Thurs 7-9 PM
'''

#main
if __name__ == '__main__':
    while True:
        testscores = [ ]
        print("Enter test scores between 0 and 100. Enter -1 to quit: ")

        #sets -1 as terminating value
        while True:
            score = int(input( ))
            if score == -1:
                break
            testscores.append(score)

        print("Enter file name: " , end = '')
        fileName = input( )  # read file name

        #terminates program if file name is empty
        if len(fileName) == 0:
            break

        #secures files as .txt
        if not fileName.endswith('.txt'):
            fileName += '.txt'

        #open new file and input values
        file = open(fileName , 'w+')
        for score in testscores:
            file.write(str(score) + '\n')
        file.close()

        #option to add new test scores into new file or end program
        print("Please answer to either add new scores into a new file (y) or end program entirely (n): " , end ='')
        testscores2 = input()
        if testscores2.lower() == 'n':
            break