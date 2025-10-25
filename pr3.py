def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes 
def  minutes_to_seconds(minutes):
    seconds = minutes * 60 
    return seconds
def total_seconds(hours, minutes, seconds):
    total = hours * 60*60 + minutes *60 + seconds
    return total 
def  format_time(total_minutes):
    hours = total_minutes // 60 
    minutes = total_minutes % 60 
    return hours , minutes 
def can_fit_task(available_hours, task_hours, task_minutes):
    available_minutes  = available_hours * 60 
    task_total_minutes  = task_hours * 60 + task_minutes
    return  task_total_minutes <= available_minutes
def schedule_summary(task_name, hours, minutes) :
task_name = input("enter the name :")
    

