def hours(duration):
    hours = duration // 3600
    return hours

def minutes(duration):
    minutes = (duration - (3600 * hours(duration))) // 60
    return minutes

def seconds(duration):
    seconds = (duration - (3600 * hours(duration))) % 60
    return seconds