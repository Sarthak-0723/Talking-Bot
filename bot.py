# © 2023 Sarthak Raut
import openai
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

engine = pyttsx3.init()
listener = sr.Recognizer()
openai.api_key = "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"

while True:
    with sr.Microphone() as source:
        print("Speak now....")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        model = "text-davinci-003"    
         
    
    if "exit" in data:
        break
    if 'play' in data:
        song = data.replace('play', '')
        engine.say('playing ' + song)
        pywhatkit.playonyt(song) 
        engine.runAndWait()
        break
    if 'who made you' in data:
        print("I am created by sarthak raut")
        engine.say("I am created by sarthak raut")
        engine.runAndWait()
        continue
    if 'who is your owner' in data:
        print("I am created by sarthak raut")
        engine.say("I am created by sarthak raut")
        engine.runAndWait()
        continue
    elif 'current time' in data:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print("You said: " + data)
        print( "sam said: " + time)
        engine.say('Current time is ' + time)
        engine.runAndWait()
        continue
   

    completion = openai.Completion.create(model = "text-davinci-003",
        prompt = data,
        max_tokens = 1024,
        temperature = 0.5,
        n = 1,
        stop = None)

    response = completion.choices[0].text
    print("You said: " + data)
    print("sam said: " + response)
    engine.say(response)
    engine.runAndWait()
