from time_module import get_hours, get_date
from output_module import output
import database
from datetime import date

def greet():

    previous_date = database.get_last_seen()

    today_date = get_date()
    database.update_last_seen(today_date)
    
    output("Hello! This is your Personal Desktop Assistant:")
    if previous_date == today_date:
        output("Welcome back Sir!")

    else:
        hour = int(get_hours())

        if hour >=4 and hour < 12:
            output("Good Morning, Sir!")
        elif hour >=12 and hour< 16:
            output("Good Afternoon, Sir!")
        else:
            output("Good evening, Sir!")

