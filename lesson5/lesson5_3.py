empl = {'Rabbit': 25, 'Smith': 7, 'Trin':9}

with open("5_3.txt", 'w') as file_obj:
    for last_name, salary in empl.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
summa = 0
count = 0
pers = []
with open("5_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        i = line.split(':')
        if int(i[1]) <= 20:
            pers.append(i[0])
        summa += int(i[1])
        count += 1
result = summa / count
print(f"employers: {pers}")
print(f"av: {result}")


