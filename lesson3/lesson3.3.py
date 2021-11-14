def my_func(number_1, number_2, number_3):
    summ = number_1+number_2+number_3
    return summ - min((number_1, number_2 , number_3))


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
result = my_func(a, b, c)
print(result)


