
def add_time(start, duration, day=None):

    day_index = 0
    time = ''
    meridian = ''
    meridian_switch = 0
    end_day = ''
    end_day_count = 0
    week_days = ['Sunday', 'Monday', 'Tuesday',
                 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day is not None:
        day_index = week_days.index(day.capitalize())

    am_pm = start.split(' ')[1]

    sart_hour = start.split(' ')[0].split(':')[0]
    sart_minute = start.split(' ')[0].split(':')[1]
    duration_hour = duration.split(':')[0]
    duration_minute = duration.split(':')[1]

    new_hour = int(sart_hour) + int(duration_hour)
    new_minute = int(sart_minute) + int(duration_minute)

    if new_minute > 60:
        new_hour = new_hour + 1
        new_minute = new_minute % 60

    if len(str(new_minute)) < 2:
        new_minute = '0' + str(new_minute)

    while new_hour >= 12:
        new_hour = new_hour - 12

        if am_pm == 'PM':
            am_pm = 'AM'
            meridian_switch += 1
        else:
            am_pm = 'PM'

        meridian_switch += 1

        if meridian_switch >= 2:
            end_day_count += 1
            meridian_switch = 0
            day_index += 1
            if day_index == len(week_days) or day_index > len(week_days):
                day_index = 0

    if new_hour == 0:
        new_hour = '12'

    if end_day_count == 1:
        end_day = 'next day'
    elif end_day_count > 1:
        end_day = f'{end_day_count} days later'
    elif end_day_count == 0:
        end_day = day

    meridian = am_pm

    if day is None and end_day_count > 0:
        time = f'{new_hour}:{new_minute} {meridian} ({end_day})'
        return time
    if day is None:
        time = f'{new_hour}:{new_minute} {meridian}'
        return time
    if day is not None and end_day_count == 0:
        time = f'{new_hour}:{new_minute} {meridian}, {week_days[day_index]}'
        return time
    else:
        time = f'{new_hour}:{new_minute} {meridian}, {week_days[day_index]} ({end_day})'

    return time


result = add_time('2:59 AM', '24:00', 'saturDay')

print(result)
