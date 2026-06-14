class Calculator:
    def __init__(self):
        self.history_file = "history.txt"

    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0: return "Error: Division by zero"
        return a / b

    def save_to_history(self, expression, result):
        with open(self.history_file, "a") as f:
            f.write(f"{expression} = {result}\n")

    def show_history(self):
        try:
            with open(self.history_file, "r") as f:
                print("\n--- Calculation History ---")
                print(f.read())
        except FileNotFoundError:
            print("\nHistory is empty.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    calc = Calculator()
    while True:
        print("\n--- Professional Calculator ---")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History\n6. Exit")
        choice = input("Select an option (1-6): ")

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == '1': res = calc.add(num1, num2); op = "+"
            elif choice == '2': res = calc.subtract(num1, num2); op = "-"
            elif choice == '3': res = calc.multiply(num1, num2); op = "*"
            elif choice == '4': res = calc.divide(num1, num2); op = "/"
            
            print(f"Result: {res}")
            calc.save_to_history(f"{num1} {op} {num2}", res)
            
        elif choice == '5':
            calc.show_history()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
