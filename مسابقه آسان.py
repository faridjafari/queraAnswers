import math

user_input = input()
num_data = user_input.split()

if len(num_data) != 2:
    print()
else:
    try:
        n = int(num_data[0])
        given_num = int(num_data[1])
        factorial = math.factorial(n)


        def num2array(number):
            return [int(digit) for digit in str(number)]

        array = num2array(factorial)
        x = array.count(given_num)
        print(x)
    except ValueError:
        print("Please enter valid integers.")
