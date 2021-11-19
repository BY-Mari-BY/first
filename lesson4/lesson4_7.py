def fact(num):
    curr = 1
    for i in range(1, num + 1):
        curr *= i
        yield curr

n = 7
for x, el in enumerate(fact(n)):
    print(f"{x + 1} {el}")


