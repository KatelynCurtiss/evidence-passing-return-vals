# Katelyn Curtiss
# January 10 2024
# Quiz

def square_number(num1):
    return num1 ** 2
    #return num1 * num1

def add_squares(num1, num2):
    # add_squares()
    # add_squares()
    num1_squared = square_number(num1)
    num2_squared = square_number(num2)
    total = num1_squared + num2_squared
    return total

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = add_squares(num1, num2)

    print(f'The sum of the squares of {num1} and {num2} is: {result}')


if __name__ == '__main__':
    main()
