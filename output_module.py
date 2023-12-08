import assistant_details
import win32com.client
# from speak_module import speak
# from database import speak_is_on

def output(o):

    #command line output

    # if speak_is_on():
    #     speak(o)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    print(assistant_details.name+ ": " +o)
    speaker.Speak(o)
    print()

    