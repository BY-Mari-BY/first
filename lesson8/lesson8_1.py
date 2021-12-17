class Data:
    def __init__(self, day_month_year):

        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right'
                else:
                    return f'Wrong year'
            else:
                return f'Wrong mounth'
        else:
            return f'Wrong day'

    def __str__(self):
        return f'Today is {Data.extract(self.day_month_year)}'


today = Data('22 - 2 - 2013')
print(today)
print(Data.valid(7, 10, 2034))
print(today.valid(11, 23, 2016))
print(Data.extract('04 - 12 - 2021'))
print(today.extract('10 - 12 - 2021'))
print(Data.valid(1, 12, 2021))

