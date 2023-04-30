import speech_recognition as sr
import pyaudio

if __name__ == '__main__':

    recognizer= sr.Recognizer()
    mic = sr.Microphone(1)
    print("Running")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, 1)  # Adjust for ambient
        print("Say something!")
        audio = recognizer.listen(source)
        #lst = audio.split()
        #print(lst)
        #stringAudio = str(audio)
        #print(stringAudio)
    print("Runnnnnn")
    try:
        print("Analyzing voice data  " + (recognizer.recognize_google(audio, language='en-US')))
        print(type((recognizer.recognize_google(audio, language='en-US'))))
    except Exception:
        print("Something went wrong")