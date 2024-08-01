
from datetime import datetime
from datetime import timedelta

date_format = "%d.%m.%Y"
#returns day to congratulate user depending of his birthday
def get_upcoming_birthdays_users(users):
    users_to_congratulate = []
    for user in [u for u in users if u.birthday]:
        if (is_birthday_within_next_seven_days(get_this_year_birthday(user.birthday.value))):
            users_to_congratulate.append(user)
    return users_to_congratulate

#to compare with todays date we need a date wtih this year
def get_this_year_birthday(user_birthday_date) -> datetime:
    today_date = datetime.today().date()
    try:
        return datetime(today_date.year, user_birthday_date.month, user_birthday_date.day).date()
    except: 
        return None

def is_birthday_within_next_seven_days(user_birthday_date):
    today_date = datetime.today().date()
    days_diff = (user_birthday_date - today_date).days
    return days_diff >= 0 and days_diff < 7

def get_congratulation_date(user_birthday_date):
    user_birthday_date = get_this_year_birthday(user_birthday_date)
    day_number = user_birthday_date.weekday() + 1
    if (day_number) > 5:
        offset = 8-day_number
        user_birthday_date = user_birthday_date + timedelta(days=offset)
    return user_birthday_date

def get_next_week_dates():
    today = datetime.today()
    days_until_next_monday = (7 - today.weekday()) % 7
    next_monday = today + timedelta(days=days_until_next_monday)
    next_week = [next_monday + timedelta(days=i) for i in range(7)]
    return next_week