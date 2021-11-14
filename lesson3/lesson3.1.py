def div_elem(a,b):
    if b==0:
        return 'Its impossible'
    else:
        return a/b
a = float(input("a: "))
b = float(input("b: "))
print(div_elem(a,b))
