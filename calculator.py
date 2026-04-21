def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    print("Simple Calculator")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")
    print("Enter 'q' to quit")

    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op.lower() == 'q':
            break
        if op not in operations:
            print("Invalid operation. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue

        result = operations[op](a, b)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()