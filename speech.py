# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:13:02 2023

@author: rohan
"""
import speech_recognition
import sys
#read duration from the arguments
duration = 5
rec = speech_recog.Recognizer()
print("Please talk")
with speech_recog.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = rec.record(source, duration=duration)
    print("Recognizing...")
    # convert speech to text
    text = rec.recognize_google(audio_data)
    print(text)