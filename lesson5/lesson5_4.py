my_dict = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
result = []

with open("5_4_out.txt", 'r') as file_obj:

    for i in file_obj:
         i = i.split(" - ")
         print(i)

if i [0] in my_dict:
    word = my_dict[i[0]]
    result.append(word + '-' + i[1])
    print(result)

with open("5_4_in.txt", "w") as file_obj_2:
    content = file_obj_2.writelines(result)






