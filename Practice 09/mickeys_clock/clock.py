
from datetime import datetime


def get_clock_angles(now=None):
    if now is None:
        now = datetime.now()

    minutes = now.minute
    seconds = min(now.second, 59)

    minute_angle = (minutes + seconds / 60) * 6
    second_angle = seconds * 6

    return minute_angle, second_angle
