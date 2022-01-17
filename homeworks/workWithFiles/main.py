while True:
    num1 = int(input(" Enter the first number: "))
    operator = input(" Enter operator: ")
    num2 = int(input(" Enter the second number: "))
    total = num1 + num2
    deduct = num1 - num2
    multiple = num1 * num2
    division = num1 / num2

    if operator == "+":
        print(total)
        with open('result.txt', 'a') as file:
            file.write(f"\n{num1} {operator} {num2} = {total}")
    elif operator == "-":
        print(deduct)
        with open('result.txt', 'a') as file:
            file.write(f"\n{num1} {operator} {num2} = {deduct}")
    elif operator == "*":
        print(multiple)
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {operator} {num2} = {multiple} "))

    elif operator == "/":
        print(int(division))
        with open('result.txt', 'a') as file:
            file.write(str(f"\n {num1} {operator} {num2} = {division} "))
    else:
        print("Invalid operator")
