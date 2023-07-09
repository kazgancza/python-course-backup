def convertToSeconds(hours, minutes):
    seconds = hours * 3600 + minutes * 60
    return seconds

print(convertToSeconds(3, 25))

def convertToHours(minutes):
    hours = minutes / 60
    return hours

print(convertToHours(120))