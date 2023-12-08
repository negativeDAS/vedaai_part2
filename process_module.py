from output_module import output
from time_module import get_time, get_date
from input_module import take_input
from database import *
import webbrowser
from internet import check_internet_connection, check_on_wikipedia
import assistant_details

def process(query):

    answer = get_answer_from_memory(query)

    if answer == 'get time details':
        return ("Time is " + get_time())
    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    
    elif answer == "tell date":
        return "Date is " + get_date()
    
    elif answer == "web search":
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org/"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in answer.lower():
                output(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        return "Opened Sir!"
        
    elif answer == 'change name':
        output("Okay! what do you want to call me?")
        temp = take_input()
        if temp == assistant_details.name:
            return 'What was to change here?'
        else:
            update_name(temp)
            assistant_details.name = temp
            return f"Now you can call me {temp}"
    elif answer == "shut down":
        exit()
    else:
        output("I do not understand this one, should I search this on internet?")
        output("Listening...")
        ans = input("Yes or No")
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        else: 
            output("Can you please tell me what it means ?")
            output("Listening...")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "")
                ans = ans.strip()

                value = get_answer_from_memory(ans)
                if value == "":
                    return "Can't help with this one!"
                else:
                    insert_question_and_answer(query, value)
                    return "Thanks I will remember this the next time"
            
            else:
                return "Can't help with this one!"



        return "nothing to return for now"
