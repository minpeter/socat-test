userInput = input("Enter a number: ")

try:
    userInput = int(userInput)
    if userInput == 1395:
        print("flag{you_entered_the_correct_number}")
    else:
        print("You did not enter the correct number")
except ValueError:
    print("You did not enter a number!")
