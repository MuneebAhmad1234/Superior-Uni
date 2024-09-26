import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

while True:
    user_input = input("Enter a number (enter 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    if user_input.isdigit():
        num = int(user_input)
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    else:
        print("Please enter a valid number.")
