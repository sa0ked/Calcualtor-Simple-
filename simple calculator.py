import time

def menu():
    print(
        "HI ITS CALCULATOR!\n"
        "1. Start\n"
        "2. Exit\n"
        "3. About"
    )

def start():
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return

    operation = input("Enter the operation (+, -, *, /): ")
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2
    else:
        print("Error: Invalid operation selected!")
        return

    print(f"The result is: {result}")

def about():
    print("This is a simple calculator program created by Sa0ked.")
    time.sleep(1)
    print("This program can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.")
    time.sleep(1)
    print("Version: 1.0")
    time.sleep(2)

def main():
    while True:
        menu()
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            start()
        elif choice == "2":
            print("Exiting the program...")
            time.sleep(1)
            break
        elif choice == "3":
            about()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()