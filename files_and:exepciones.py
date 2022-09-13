#files and exeptions
#reading from a file



from logging import exception

#working with Multiple Files
def count_word(filename):

    try:
        with open(filename) as file:
            read_data = file.read()
    except: 
        print("file not found\n")
    else:
        word = read_data.split()
        num_word = len(word)
        print("the file havea wordssssssssssss: ",num_word)




def main():
    print("hola")
    with open('file.txt') as file_object:
        contents = file_object.read() # asigna el contenido a un objeto
    print(contents)
    #"BREAK CLOSE ARCHIVO"<-----this archive is close when finally finish bloq of with

#file path    
    file_path = '/home/daniel/Desktop/Proyect_Aeiou052/crash_course_a_hands_on.py/file.txt'
    with open(file_path) as file_object:
         contents2 = file_object.read() # asigna el contenido a un objeto
    print(contents2.rstrip())

#Reading line by line
    filename = 'file.txt'
    with open(filename) as file_object:
        print("reading echa line through for:\n")
        for line in file_object: #for examine each line through for 
            print(line.rstrip())

#Making a file's Contents

    print("making a files contents")
    
    filename = 'file.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    
    pi_string = ''
    for line in lines:
        pi_string += line.strip() #managaments lines and delete space blank
        
    print(pi_string)
    print(len(pi_string))

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip() #managaments lines and delete space blank
    print(pi_string)
    print(len(pi_string))

#large Files: One Milion Digits
    filename = 'file.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(pi_string[:52])
    print(len(pi_string))

#Is Your Birthday Contained in Pi?
    # filename = 'file.txt'
    # with open(filename) as file_object:
    #     lines = file_object.read()

    #     pi_string += lines.strip()

    # for line in lines:
    #     pi_strings += lines.strip()
        
    #     bir = input("enter your date birth: ")

    #     if line.startswith('1509'):
    #         print("your birth appers in the first million digits of pi!")
    #         print(line)
    #     else:
    #         print("Your birthday is not in PI!")
    #         continue

#writing to an file Empty File
    filename = 'programing.txt'
    with open(filename, 'w') as file_object:
        file_object.write("Hi Daniel.\n")

#writing multiples Lines
        file_object.write("in try create and modific new files\n")

#appending to a file
    filename = 'programing.txt'
    with open(filename, 'a') as file_object:
        file_object.write("open fiel to edit file\n")
        file_object.write("here example\n")

#Exceptions
#Handling the ZeroDivisionError Exception
#using try_except Blocks

#Using Execption to Prevent Crashes
    print("Give me two numbers, and i'all divide them")
    print("Enter 'q' to quit")

    # while True:
    #     first_number = input("first number")
    #     if first_number == 'q':
    #         break
    #     second_number = input("Second number:")
    #     if second_number == 'q':
    #         break
    #     try:
    #         answer=int(first_number)/int(second_number)
    #     except ZeroDivisionError:
    #         print("you cant do it")
    #     else:
    #         print(answer)


#Handling the fileNotFoundError Exception
    filename= 'alice.txt'
    try:
        with open('alice.txt') as file:
            read_data = file.read()
    except:
        print('sorry but dont found file')
    
#Analizing Text
    Title = "dANIEl suarez nava"
    Title.split()
    print(Title)


    filename = '/home/daniel/Desktop/Proyect_Aeiou052/crash_course_a_hands_on.py/programing.txt'
    try:
        with open('programing.txt') as file:
            read_data = file.read()
    except: 
        print("file not found\n")
    else:
        word = read_data.split()
        num_word = len(word)
        print("the file havea words: ",num_word)

    filenames = ['programing.txt','file.txt']
    for filename in filenames:

        count_word(filename)


#Failing Silently
    
    




if __name__ == "__main__":
    main()
