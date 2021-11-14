def int_func(txt):
    word=txt[0].upper() + txt[1:]
    return word

my_str = input("Enter words by space: ")
for word in my_str.split(' '):
    print(f'{int_func(word)}', end=' ')