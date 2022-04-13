# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:45:58 2022

@author: 77469
"""
# curl --request POST \
#   --url http://localhost:5005/webhooks/rest/webhook \
#   --header 'content-type: application/json' \
#   --data '{"sender": "sender_id", "message": "hi"}'
  
  
# import time
import requests
from requests.structures import CaseInsensitiveDict
import speech_recognition as sr
# import msvcrt
# import os
from playsound import playsound
# from pydub import AudioSegment
# from pydub.playback import play
import gtts
def request(text):
    url = 'http://localhost:5005/webhooks/rest/webhook'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"sender": "sender_id", "message": "' + text + '"}'
    r = requests.post(url, headers = headers, data = data)
    L = []
    for item in r.json():
        L.append(item['text'])
    return L

def speech_to_text():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    text = r.recognize_google(audio)
    return text

def play_wav():
    try:
        playsound(r"C:/Users/77469/Music/test.mp3")
        # play(AudioSegment.from_mp3("C://Users//77469//Music//test.wav"))
    except:
        play_wav()
    # playsound(r"C:/Users/77469/Music/test.mp3")


def chatbot_text(text):
    path = r"C:/Users/77469/Music/test.mp3"
    r = request(text)
    tts_text = ''
    for a in r:
        # print("VA: " + a)
        a = a.strip('/n')
        for s in a:
            if s not in ['^', '_', '(', ')']:
                tts_text += s
    # print(tts_text)
    
    tts = gtts.gTTS(tts_text)
    tts.save(path)
    play_wav()
    return(tts_text)

def chatbot_speech():
    path = r"C:/Users/77469/Music/test.mp3"
    text = speech_to_text()
    r = request(text)
    tts_text = ''
    for a in r:
        # print("VA: " + a)
        a = a.strip('/n')
        for s in a:
            if s not in ['^', '_', '(', ')', "'", "`", '>', '<', '*', '﹏']:
                tts_text += s
    # print(tts_text)
    tts = gtts.gTTS(tts_text)
    tts.save(path)
    # time.sleep(1)
    play_wav()
    return(text, tts_text)

def speak_text(text):
    path = r"C:/Users/77469/Music/test.mp3"
    tts = gtts.gTTS(text)
    tts.save(path)
    play_wav()


# if __name__ == "__main__":
#     path = r"C:/Users/77469/Music/test.mp3"
#     # os.remove(path)
#     # os.remove("C://Users//77469//Music//test.mp3")      
#     while 1:
#         # os.remove("C://Users//77469//Music//test.mp3")
#         # text = input("Your input: ")
#         text = speech_to_text()
#         print("Your input: " + text)
#         r = request(text)
#         tts_text = ''
#         for a in r:
#             print("VA: " + a)
#             a = a.strip('/n')
#             for s in a:
#                 if s not in ['^', '_', '(', ')']:
#                     tts_text += s
#         # print(tts_text)
#         tts = gtts.gTTS(tts_text)
#         tts.save(path)
#         # time.sleep(1)
#         play_wav()
#         if text == '/stop' or text == 'bye':
#             break
#         print("--------------Press 'Enter' to continue--------------")
        
#         while True:
#             if input() == '':
#                 break
            
            