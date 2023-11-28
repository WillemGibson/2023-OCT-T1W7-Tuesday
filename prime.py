# If a number is prime or not

def is_prime(number):
    for i in range(2, number):
        if (number % i == 0):
            print("Not a prime")
            break
    else:
        print("A prime")

is_prime(11)