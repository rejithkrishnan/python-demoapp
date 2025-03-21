def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        raise ValueError("Invalid number input")

def calculator():
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1-4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1, num2 = get_numbers()
        
        if choice == '1':
            return num1 + num2
        elif choice == '2':
            return num1 - num2
        elif choice == '3':
            return num1 * num2
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero")
                return None
            return num1 / num2
    else:
        print("Invalid choice")
        raise ValueError("Invalid operation choice")

if __name__ == "__main__":
    print(calculator())