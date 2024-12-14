import speech_recognition as sr

def recognize_speech():
    """Recognize speech using the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            print("Processing...")
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return "No audio inputted by user."
        except sr.RequestError:
            print("Recognition request failed.")
