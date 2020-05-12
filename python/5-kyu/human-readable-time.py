def make_readable(seconds):
    hours = seconds // 3600
    remaining_time = seconds - (hours * 3600)
    minutes = remaining_time // 60
    seconds = remaining_time - (minutes * 60)
    if hours < 10:
        hours = "0" + str(hours)
    else:
        hours = str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    return hours + ":" + minutes + ":" + seconds

result = make_readable(4500)
print(result)