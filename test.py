# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H hours %M minutes")
# print("Current Time=", current_time)


# from datetime import date
# today = date.today()
# print("Today's date:", today)

# from gtts import gTTS

# tts = gTTS('Hello')
# tts.save('hello.mp3')

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    s = input()
    speaker.Speak(s)