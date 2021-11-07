print("Good day")
number_n = int(input("Tell me your number"))
max = 0
while number_n > 0:
    if number_n % 10 > max:
        max = number_n % 10
    number_n //= 10
print(f"Maximum: {max}")
