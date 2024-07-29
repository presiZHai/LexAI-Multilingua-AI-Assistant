import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS
from dotenv import load_dotenv

#GOOGLE_API_KEY = "****************************"
# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def voice_input():
    # Create a recognizer instance
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)  # Using Google Speech Recognition
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
def text_to_speech(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')  # Language can be changed

    # Save the audio as an MP3 file
    tts.save("speech.mp3")

def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    response=model.generate_content(user_text)
    
    result=response.text
    
    return result
