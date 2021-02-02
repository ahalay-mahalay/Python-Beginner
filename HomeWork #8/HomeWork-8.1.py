# 1. Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        while True or date != "q":
            try:
                day, month, year = [int(i) for i in date.split("-")]
            except ValueError:
                print("Day, month, year must be an integer!")
                date = input("Enter date in format DD-MM-YYYY: ")
                if date == "q":
                    break
            else:
                date = [day, month, year]
                break

        return cls(date)
        # return cls.validation(date)

    @staticmethod
    def validation(obj):
        day = obj.date[0]
        month = obj.date[1]
        year = obj.date[2]
        days_in_a_month = {1: 31, 2: [28, 29], 3: 31,
                           4: 30, 5: 31, 6: 30,
                           7: 31, 8: 31, 9: 30,
                           10: 31, 11: 30, 12: 31}
        leap_year = year % 4 == 0
        if month not in range(1, 13):
            return f"Month number is not valid!\nYou've entered {month}!"
        for _ in days_in_a_month:
            if month == 2:
                if (leap_year and day > days_in_a_month[2][1]) \
                        or (not leap_year and day > days_in_a_month[2][0]):
                    return f"For the {month} month the day is not valid!\nYou've entered {day}!"
            elif day > days_in_a_month[month]:
                return f"For the {month} month the day is not valid!\nYou've entered {day}!"
        return "Date is valid!"


my_date = "29-02-2020"
my_1 = Date.date_to_int(my_date)
print(*my_1.date, sep="-")
try:
    print(my_1.validation(my_1))
except IndexError:
    print("You are out. Goodbye!")
