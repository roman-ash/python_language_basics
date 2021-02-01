import datetime


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self

    @classmethod
    def to_int(cls, date):
        return [int(i) for i in date.split("-")]

    @staticmethod
    def is_valid(date):
        day, month, year = date.split("-")
        is_valid_date = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            is_valid_date = False
        if is_valid_date is True:
            return "Date is valid."
        else:
            return "Date is not valid."


print(Date.to_int("01-10-1996"))
print(Date.is_valid("01-10-1996"))
print(Date.is_valid("31-02-2001"))
