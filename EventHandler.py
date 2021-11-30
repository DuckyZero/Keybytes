import os
import speech_recognition as sr
from pygame import *

class SpeechHandler:

    def __init__(self):
        self.word_list = None

    def speech_to_list(self):

        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)

            print("\nPlease say the sound file path: ")

            audio = r.listen(source)

            try:
                sound_path = str(r.recognize_google(audio))
                # self.word = sound_path
                self.word_list = sound_path.split(" ")
                return self.word_list



            except Exception as e:
                print('error')

class menu:

    def print_menu(self):
        print('\n[1]: Create Keybyte')
        print('[2]: List Keybytes')
        print('[3]: Delete Keybyte')
        print('[`]: Toggle Speech-To-Play')
        print('[4]: Exit Program')

        print("\nPlease enter a number/symbol as shown above: ")
