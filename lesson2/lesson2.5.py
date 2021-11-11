my_list = [7, 5, 3, 3, 2]
rating = int(input('Enter new rate '))
yes = False
for pos, rate in enumerate(my_list):
    if rating > rate:
        my_list.insert(pos,rating)
        yes = True
        break
if not yes:
    print(my_list)

print(my_list)
