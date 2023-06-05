# Ask user if they want to use their own file to do calculations from

file_input = input("Would you like to use an existing file of calculations? Please enter either yes or no: ")

while True:
    if len(file_input) == 2:
        print("Thank you for using this calculator. Have a nice day! \n")
    elif len(file_input) == 3:

# Ask them to input the name of their file, add '.txt' to get correct format to open file
# If incorrect name they will be prompted to try again by the except parameter

        try:
            file_name = input("Please enter the name of your file: ") +".txt"
            open_file = open(file_name, 'r')
            user_file = open_file.read( )
            print(user_file)        
            break
        except FileNotFoundError as error:
            print("\n")
            print(error)
            print("Invalid entry. Please ensure you have correctly entered the name of your file without any mistakes. \n")



