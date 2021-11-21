my_list = ['First\n', 'Second\n', 'Third\n']

with open("5_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("5_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("/n")
        letters = len(line) - 1
        print(f"Letters in line = {letters}")
        print(f"Number of strings = {lines} ")

