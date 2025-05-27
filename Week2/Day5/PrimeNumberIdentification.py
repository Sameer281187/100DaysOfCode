def is_prime(num):
    if num == 1:
        return False
    elif num < 4:
        return True
    else:
        prime_or_not = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                prime_or_not = False
                break

        return prime_or_not

number = int(input("Enter a number: "))
result = print(f"{number} is a prime number.") if is_prime(number) else print(f"{number} is not a prime number.")