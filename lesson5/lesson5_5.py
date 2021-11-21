
with open('5_5.txt', 'w+') as file_obj:
    line = input('Enter numbrs throu space \n')
    file_obj.writelines(line)
    summ = line.split()

    print(sum(map(int, summ)))

