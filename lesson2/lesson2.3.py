print('Hello ')
# month = list(range(1,13))
# print(month)
# my_str_1 = int(input('Please choose the number of the month'))
# h, p , s , a = 'winter', 'spring', 'summer', 'autumn'
# seasons = [h,h,p,p,p,s,s,s,a,a,a,h]
# ordering = {'1':h, '2':h, '3':p, '4':p, '5':p, '6':s, '7':s, '8':s, '9':a, '10':a, '11':a, '12':h}
# print('Its', seasons[int(my_str_1)-1], '!')

my_str_1 = input('Please enter the number of the month')
h, p , s , a = 'winter', 'spring', 'summer', 'autumn'
seasons = [h,h,p,p,p,s,s,s,a,a,a,h]
ordering = {'1':h, '2':h, '3':p, '4':p, '5':p, '6':s, '7':s, '8':s, '9':a, '10':a, '11':a, '12':h}
print(seasons[int(my_str_1)])
