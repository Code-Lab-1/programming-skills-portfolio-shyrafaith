#a1 exercise 2-done
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Welcome to Python Calculator")
print("In order to start, select a operation.")
print("Please note that only press the number of the operation of your choice. ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    
        next_calculation = input("Would you like to use the calculator again? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input!!!")