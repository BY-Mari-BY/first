my_list = []
while True:
    a = input("Print smth: ")
    if a == '':
        print(my_list)
        exit()
    else:
        new_line = a + '/n'
        my_list.append(new_line)

with open('5_1_new.txt', 'w') as file_obj:
    file_obj.writelines(my_list)

