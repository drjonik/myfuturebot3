import re

WEEKDAYS = {
    "понедельник": "Пн",
    "вторник": "Вт",
    "среда": "Ср",
    "четверг": "Чт",
    "пятница": "Пт",
    "суббота": "Сб",
    "воскресенье": "Вс"
}

def parse_human_time(text: str):
    match = re.search(r"(кажд(ый|ую)\s+(?P<day>понедельник|вторник|среда|четверг|пятница|суббота|воскресенье))\s+в\s+(?P<time>\d{1,2}:\d{2})\s+(?P<task>.+)", text.lower())
    if not match:
        return None
    day = match.group("day")
    time = match.group("time")
    task = match.group("task")
    return task.capitalize(), WEEKDAYS.get(day, ""), time