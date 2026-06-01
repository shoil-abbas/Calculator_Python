def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error! Cannot divisible by zero."
    return num1 / num2

print("=== Calculator ===")
while True:
    print("\n1. Addition \n2. Subtraction \n3. Multiply \n4. Division \n5. Exit")
    choice = input("Choose the Operation : ")

    if choice == '5':
        print("GoodBye! Exiting....")
        break
    if choice in ['1','2','3','4']:
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
            match choice:
                case '1':
                    print("Result : ", add(num1, num2))
                case '2':
                    print("Result : ", sub(num1, num2))
                case '3':
                    print("Result : ", mul(num1, num2))
                case '4':
                    print("Result : ", div(num1, num2))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    
    else:
        print("Invalid choice! Try again")