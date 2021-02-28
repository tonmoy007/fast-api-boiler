import datetime
from typing import List
from dateutil.relativedelta import relativedelta
import calendar


class DateRange:
    start: datetime.datetime
    end: datetime.datetime

    def __init__(self, start: datetime.datetime, end: datetime.datetime):
        self.start = start
        self.end = end

    @classmethod
    def for_today(cls):
        return DateRange.for_a_day(datetime.datetime.today())

    @classmethod
    def for_yesterday(cls):
        return DateRange.for_a_day(yesterday())

    @classmethod
    def for_a_day(cls, date: datetime.date):
        return DateRange.of_dates(date, date)

    @classmethod
    def for_a_month(cls, date: datetime.date):
        first_day = date.replace(day=1)
        last_day = date.replace(day=calendar.monthrange(date.year, date.month)[1])
        return DateRange.of_dates(first_day, last_day)

    @classmethod
    def of_dates(cls, start: datetime.date, end: datetime.date):
        start = datetime.datetime(start.year, start.month, start.day, 0, 0, 0)
        end = datetime.datetime(end.year, end.month, end.day, 23, 59, 59)
        return DateRange(start, end)

    def get_duration_in_days(self) -> int:
        return (self.end - self.start).days

    def get_dates(self) -> List[datetime.datetime]:
        d = self.get_duration_in_days()
        dates = []
        for i in range(d + 1):
            dates.append(self.start + datetime.timedelta(days=i))
        return dates

    def contains_today(self):
        return self.contains(datetime.datetime.today().date())

    def contains(self, date: datetime.date):
        return self.start.date() <= date <= self.end.date()

    def is_single_day(self):
        return self.get_duration_in_days() is 0

    def is_week(self):
        return 0 < self.get_duration_in_days() < 15

    def is_month(self):
        return 15 < self.get_duration_in_days() < 32

    def get_first_dates_of_months(self) -> List[datetime.datetime]:
        dates = []
        date = self.start
        while date <= self.end:
            dates.append(datetime.datetime(date.year, date.month, 1))
            date += relativedelta(months=1)
        return dates

    def get_first_hours(self) -> List[datetime.datetime]:
        dates = []
        date = self.start
        while date <= self.end:
            dates.append(datetime.datetime(date.year, date.month, date.day, date.hour, 0, 0))
            date += relativedelta(hours=1)
        return dates

    @property
    def __to_date_dict__(self):
        return {
            'start': format_date(self.start.date()),
            'end': format_date(self.end.date())
        }

    @property
    def __to_dict__(self):
        return {
            'start': format_datetime(self.start),
            'end': format_datetime(self.end)
        }


def format_datetime(value: datetime.datetime):
    if value is None:
        return None
    elif type(value) == str:
        return value
    return value.strftime("%Y-%m-%d %H:%M:%S")


def format_date(value: datetime.date):
    return value.strftime("%Y-%m-%d")


def yesterday() -> datetime.date:
    return datetime.date.today() - datetime.timedelta(days=1)


def get_start_end_for_a_date(date: datetime.date) -> DateRange:
    return DateRange.for_a_day(date)


def get_start_end_for_a_month(date: datetime.date) -> DateRange:
    return DateRange.for_a_month(date)
