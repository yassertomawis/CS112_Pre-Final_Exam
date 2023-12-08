print("COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Tomawis, Yasser M.")


# Determine if the given number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Find and display prime numbers in a given range
def display_primes(start, end):
    if start < 0:
        print("Enter a non-negative number.")
        return

    if end <= start:
        print("Enter a number greater than the starting range.")
        return

    primes = [num for num in range(start, end + 1) if is_prime(num)]

    print("Prime numbers in the range {} to {}:".format(start, end))
    print(primes)


# Prompt the user to enter starting and end range.
if __name__ == "__main__":
    while True:
        try:
            start_range = int(input("\nEnter the starting range (0 to terminate): "))
            if start_range == 0:
                break

            end_range = int(input("Enter the end range: "))
            display_primes(start_range, end_range)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
