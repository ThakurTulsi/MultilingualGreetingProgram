# importing speechrecognition library
# pip3 install speechrecognition
# installing python text to speech conversion pyttsx3
# pip3 install pyttsx3
# importing speechrecognition and import pyttsx3

# import speech_recognition 
import pyttsx3

# from gtts import gTTS
# # gTTS=google text to speech
# language="en"
print("Which voice assistant would you like to have? \n 1.Male 2. Female")
voiceassistant=int(input("Enter your choice: "))

# speech=gTTS(text=text, lang=language, slow=False, tld="com.au")
# speech.save("buttons.mp3")
def Female():
    print("Menu: \n1.For English 2.For hindi \n3.For French 4.To enter personalized greeting by yourself")
    button=int(input("Enter any button: "))
    if button==1:
        text="Hello"
        print("Hello")
    elif button==2:
        text="Namaste"
        print("Namaste")
    elif button==3:
        text="Bonjour!"
        print("Bonjour!") 
    elif button==4:
        text=input("enter your personalized greeting: ")   
        print(text) 
    else:
        text="Invalid button Please enter valid button Thanks"    
        print("Invalid button. Please enter valid button. Thanks") 
    
    engine=pyttsx3.init()
    voices = engine.getProperty('voices') 
    voices = engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def Male():
    print("Menu: \n1.For English 2.For hindi \n3.For French 4.To enter personalized greeting by yourself")
    button=int(input("Enter any button: "))
    if button==1:
        text="Hello"
        print("Hello")
    elif button==2:
        text="Namaste"
        print("Namaste")
    elif button==3:
        text="Bonjour!"
        print("Bonjour!") 
    elif button==4:
        text=input("enter your personalized greeting: ")   
        print(text) 
    else:
        text="Invalid button Please enter valid button Thanks"    
        print("Invalid button. Please enter valid button. Thanks") 
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if voiceassistant==1:
    Male()

elif voiceassistant==2:
    Female()  

else:
    print("Invalid option!")