def add_time(start, duration, day_of_week=''):

  num_day_of_week = 0

  if day_of_week != '':
    days_of_week = {
      'Sunday': 1,
      'Monday': 2,
      'Tuesday': 3,
      'Wednesday': 4,
      'Thursday': 5,
      'Friday': 6,
      'Saturday': 7
    }

    num_day_of_week = days_of_week[day_of_week.capitalize()]

  # Split infortmation into lists
  start_ls = start.split(' ')
  minutes_ls1 = start_ls[0].split(':')
  minutes_duration = duration.split(':')

  # Convert info into minutes
  if start_ls[1] == 'PM':
    total_minutes_start = (int(minutes_ls1[0]) + 12) * 60 + int(minutes_ls1[1])
  
  else:
    total_minutes_start = (int(minutes_ls1[0])) * 60 + int(minutes_ls1[1])
  
  total_minutes_duration = (int(minutes_duration[0])) * 60 + int(minutes_duration[1])

  total_minutes = total_minutes_start + total_minutes_duration

  #Convertion days, hours and minutes
  total_hours = total_minutes // 60
  days = total_hours // 24
  hours = total_hours % 24
  minutes = total_minutes % 60
  format_ = 'AM'
  day_week = (num_day_of_week + days) % 7
 
  if hours == 12:
    format_ = 'PM'

  if hours == 0:
    hours = 12
    format_ = 'AM'
  
  if hours > 12:
    hours -= 12
    format_ = 'PM'
  
  hours = str(hours)
  minutes = str(minutes) if minutes >= 10 else '0' + str(minutes)

  # Return String format
  if num_day_of_week == 0:
    if days == 1:
      return f'{hours}:{minutes} {format_} (next day)'
    
    if days > 1:
      return f'{hours}:{minutes} {format_} ({days} days later)'
    
    return f'{hours}:{minutes} {format_}'

  else:
    vk_day_of_week = {v:k for k,v in days_of_week.items()}
    day = vk_day_of_week[day_week]
    
    if days == 1:
      return f'{hours}:{minutes} {format_}, {day} (next day)'
    
    if days > 1:
      return f'{hours}:{minutes} {format_}, {day} ({days} days later)'
    
    return f'{hours}:{minutes} {format_}, {day}'