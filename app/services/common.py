import datetime
import json


def get_date_from_mysql_format(date: str) -> datetime.date:
    date_format = "%Y-%m-%d"
    return datetime.datetime.strptime(date, date_format).date()


def get_date_time_from_mysql_format(date: str) -> datetime.datetime:
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        return datetime.datetime.strptime(date, date_format)
    except ValueError:
        return datetime.datetime.now()


def date_to_datetime(date: datetime.date) -> datetime.datetime:
    return datetime.datetime(year=date.year, month=date.month, day=date.day)


def float_to_money(value):
    return float("{0:.2f}".format(value))


# ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])


def json_decode(data):
    try:
        return json.loads(data)
    except ValueError as e:
        return []
