import speech_recognition as sr
from time import sleep
from gtts import gTTS
import os
import pyglet
import openai

openai.api_key = "<API_KEY>"

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)

completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=text,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
answer = completion['choices'][0]['text']

tts = gTTS(text=answer)
tts.save("temp.mp3")

music = pyglet.media.load("temp.mp3", streaming=False)
music.play()
sleep(music.duration) 
os.remove("temp.mp3")