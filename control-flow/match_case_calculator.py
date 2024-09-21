num1 = int(input("Enter the first number: "))
operator = (input("Choose the operation (+, -, *, /): "))
num2 = int(input("Enter the second number: "))
result = None
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation!")
if result is not None:
    print(f"The result is {result} ")
