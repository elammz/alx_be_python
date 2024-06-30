num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operations = input("Choose the operation (+, -, *, /): ")
match operations:
    case _ if operations == "+":
        sum = num1 + num2
        print("The result is", sum, ".")
    case _ if operations == "-":
        difference = num1 - num2
        print("The result is", difference, ".")
    case _ if operations == "*":
        product = num1 * num2
        print("The result is", product, ".")
    case _ if operations == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            division = num1 / num2
            print("The result is", division, ".")

    