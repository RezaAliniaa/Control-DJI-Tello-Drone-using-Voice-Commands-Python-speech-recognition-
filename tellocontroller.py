import speech_recognition as sr
from easytello import tello 

drone = tello.Tello()

def audioRecognizer():
    speech = sr.Recognizer()
    #audio = ''

    with sr.Microphone() as source:
        print("say your command: ")
        audio = speech.listen(source,phrase_time_limit=3)
        #print("stop.")

        try:
            text = speech.recognize_google(audio,language="en-US")
            print("your command: ",text)
            #return text

        except:
            
            print("i'm waiting for your command.")
    return text


def action(input_command):
    
    if "land" in input_command:       
        drone.land()

    elif "take off" in input_command:        
        drone.takeoff()
        
    elif "forward" in input_command:
        drone.forward(30)
        
    elif "turn" in input_command or "back" in input_command:
        drone.back(30)
        
    elif "right" in input_command or "rye" in input_command:
        drone.right(30)
        
    elif "left" in input_command:
        drone.left(30)
        
    elif "see right" in input_command:
        drone.cw(30)
        
    elif "see left" in input_command:
        drone.ccw(30)
        
    elif "go up" in input_command or "up" in input_command:
        drone.up(30)
        
    elif "go down" in input_command or "dawn" in input_command or "down" in input_command:
        drone.down(30)


    else:
        pass


while True:
    
    text = audioRecognizer().lower()

    if text == 0 :
        continue

    if "bye" in str(text) or "see you later" in str(text):
        
        break

    action(text)


