from datetime import datetime, timedelta

if __name__ == '__main__':

    old_date = datetime(2011, 11, 3, 17, 23)
    print(old_date)

    print("Formatted datetime:", old_date.strftime("%d.%m.%Y. %H:%M:%S"))

    new_date = datetime(2017, 7, 12, 12, 21)
    diff_delta = new_date - old_date
    print(diff_delta.days)

    delta_13_days = timedelta(13)
    print("Day 13 days after new_date is", new_date+delta_13_days)

    date_str = "25.04.2011."
    print(datetime.strptime(date_str, "%d.%m.%Y."))
