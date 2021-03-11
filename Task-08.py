import math
def convert_to_time(time):
    hours = math.floor(time/60)
    minutes = time%60
    if hours > 1:
        hours_text = "hours"
    else:
        hours_text = "hour"
    if minutes > 1:
        minutes_text = "minutes"
    else:
        minutes_text = "minute"

    print("{} {} and {} {}".format(hours, hours_text, minutes, minutes_text))


convert_to_time(142)