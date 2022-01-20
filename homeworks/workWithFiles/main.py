num1 = input("Enter the first number: ")
operator = input("Enter operator: ")
num2 = input("Enter the second number: ")
calc = eval(num1 + operator + num2)

with open('result.txt', 'a') as file:
    file.write(f"{num1} {operator} {num2} = {calc}\n")
