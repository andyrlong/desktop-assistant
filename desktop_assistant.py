import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia
 
# Method for taking and recognizing commands
def take_command():
    
    r = sr.Recognizer()

    # Listen for command
    with sr.Microphone as source:
      print('Listening...')
      
      r.pause_threshhold = 0.7
      audio = r.listen(source)

    # Recognize speech
    try:
         print("Recognizing...")

         Query = r.recognize_google(audio, language='en-in')
         print("the command is printed=", Query)

    except Exception as e:
        print(e)
        print("Please repeat that")
        return "None"
    return Query


def speak(audio):
    
    engine =  pyttsx3.init()
    # Get method 
    voices = engine.getProperty('voices')

    # Set method
    engine.setProperty('voice', voices[0].id)

    engine.say(audio)

    engine.runAndWait()


def tell_day():

    # This method gets the day
    day = datetime.datetime.today().weekday() + 1
    
    # Dictionary that stores the days of the week
    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    
    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tell_time():

    # This method gets the time
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self, "The time is" + hour + "Hours and" + min + "Minutes")   


def hello(speak):

    # Intro voiceline
    speak("Hello, I am your desktop assistant. How may I assist you?")


def take_query():

    hello()

# Infinite loop until the user says "Bye" or terminates the program
while(True):

    query = take_command().lower()
    if "Open GitHub" in query:
        speak("Opening GitHub")
        webbrowser.open("www.GitHub.com/andyrlong")
        continue

    elif "Open Google" in query:
        speak("Opening Google")
        webbrowser.open("www.Google.com")
        continue

    elif "What day is it" in query:
        tell_day()
        continue

    elif "What time is it" in query:
        tell_time()
        continue

    elif "Bye" in query:
        speak("Goodbye")
        exit()

    elif "From wikipedia" in query:

        speak("Checking Wikipedia")
        query = query.replace("Wikipedia", "")
                
        result = wikipedia.summary(query, sentences=4)
        speak("According to Wikipedia")
        speak(result)
            
    elif "What is your name" in query:
        speak("I am Jarvis, your desktop Assistant")
    
    # Main method for executing functions
    if __name__ == '__main__':
        take_query()


