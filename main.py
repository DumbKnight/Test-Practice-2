import math


def calculator():
    print()

    action = input()

    if action != "exit":
        number1 = int(input())
        number2 = int(input())

        if action == "+":
            print(number1 + number2)
        elif action == "-":
            print(number1 - number2)
        elif action == "*":
            print(number1 * number2)
        elif action == "/":
            print(number1 / number2)
        elif action == "^":
            print(pow(number1, number2))
        elif action == "log":
            if (number1 > 0) & (number2 > 0):
                print(math.log(number1, number2))
            else:
                print("Оба значения должны быть больше 0")

        calculator()


print("Действия:"
      "\n+: сложение"
      "\n-: вычитание"
      "\n*: умножение"
      "\n/: деление"
      "\n^: степень (число, степень)"
      "\nlog: логарфим (основание, аргумент)"
      "\nexit: выход"
      "\n")

calculator()
