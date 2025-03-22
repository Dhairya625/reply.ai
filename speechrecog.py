import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Listening...")
                audio = r.listen(source2)
                Mytext = r.recognize_google(audio)
                return Mytext


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")
            
def output_text(text):
    f= open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)
    print("wrote text")

#install all these pips first
#pip install speechrecognition
# pip install pyaudio
#pip install pyttsx3
