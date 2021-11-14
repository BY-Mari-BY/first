def sum(my_str, stop):
    num_list = my_str.split(' ')
    sum_list = 0
    for s in num_list:
        if s == stop:
            break
        sum_list += int(s)
    return sum_list

breakn = '&'
fin = False
i = 0
while not fin:
    user_str = input("Enter number by space: ")
    i += sum(user_str, breakn)
    finished = breakn in user_str
    print(f"Sum = {i}")


