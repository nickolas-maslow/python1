def calc(number1, number2, operation):
    print(number1, operation, number2, '=')
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        return number1 / number2
    else:
        print('Error')
result = calc(10, 3, '+')
print(result)
result = calc(-11, -5, '-')
print(result)
