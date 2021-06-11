def calc():
    operation = input("Enter one of the operations (+-*/) or 0 to exit\n: ")
    if operation == '0':
        return "exit"
    else:
        if operation in "+-*/":
            try:
                num1 = int(input("enter the first number\n: "))
                num2 = int(input("enter the second number\n: "))
                if operation == '+':
                    result = num1 + num2
                    print(result)
                    return calc()
                elif operation == '-':
                    result = num1 - num2
                    print(result)
                    return calc()
                elif operation == '*':
                    result = num1 * num2
                    print(result)
                    return calc()
                elif operation == '/':
                    try:
                        result = num1 / num2
                        print(result)
                    except ZeroDivisionError:
                        print("Cannot be divided by 0")
                    finally:
                        return calc()
            except ValueError:
                print("Enter the number")
                return calc()
        else:
            print("Invalid character")
            return calc()


calc()
