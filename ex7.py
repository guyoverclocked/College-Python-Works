num = 10

while num > 0:
    print(num)
    num -= 1

# 2. Program: Multiplication Table for a Given Number

num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Program: Reverse the Digits of a Number

num = int(input())
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number:", reversed_num)


# 4. Program: Finding the Largest Digit in a Number

num = int(input())
largest_digit = 0

while num > 0:
    digit = num % 10
    if digit > largest_digit:
        largest_digit = digit
    num //= 10

print("Largest digit:", largest_digit)

# 5. Program: Check if a Number is Prime

num = int(input())
is_prime = True

if num > 1:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# 6. Program: Generate Prime Numbers Up to a Given Limit

limit = int(input())

for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


num = int(input())
is_prime = True

if num > 1:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")