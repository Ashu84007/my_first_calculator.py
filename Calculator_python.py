print('Welcome to this calculator!')

while(True):
    print("\n\n\nPlease choose what you want to do\n"
          "Addition: Press 1 for doing addition\n"
          "Subtraction: Press 2 for doing subtraction\n"
          "Multiplication: Press 3 for doing multiplication\n"
          "Division: Press 4 for doing division\n"
          "Exit: Press 5 for exit")


    choice = int(input())

    if(choice == 5):
        break




    if(choice == 1):
        print("Please choose your first number: ")
        num1 = float(input())
        print("Please choose your second number: ")
        num2 = float(input())
        print("Sum of", num1, "and", num2, "is:\n ", num1+num2)
    elif(choice == 2):
        print("Please choose your first number: ")
        num1 = float(input())
        print("Please choose your second number: ")
        num2 = float(input())
        print("Difference between", num1, "and", num2, "is: \n ", num1-num2)
    elif(choice == 3):
        print("Please choose your first number: ")
        num1 = float(input())
        print("Please choose your second number: ")
        num2 = float(input())
        print("After multiplying", num1, "and", num2, "answer is:\n  ", num1*num2)
    elif(choice == 4):
        print("Please choose your first number: ")
        num1 = float(input())
        print("Please choose your second number: ")
        num2 = float(input())
        print("After dividing", num1, "and", num2, "answer is:\n  ", num1/num2)

    else:
        print("Invalid choice\n ")
        break

print("Thank you for using me Have a nice Day!!!")
