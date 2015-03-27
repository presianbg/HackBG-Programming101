#!/usr/bin/python3
import datetime
import calendar


def friday_years(from_year, to_year):
    months = 12
    count_fridays = 0
    cont_friday_years = 0

    for years in range(from_year, to_year + 1):
        count_fridays = 0
        for month in range(months):
            for days in range(calendar.monthrange(years, month+1)[1]):
                if datetime.date(years, month + 1, days + 1).weekday() == 4:
                    count_fridays += 1
        if count_fridays == 53:
            cont_friday_years += 1

    return cont_friday_years

if __name__ == '__main__':
    from_year = 1753
    to_year = 2000
    print(friday_years(from_year, to_year))
