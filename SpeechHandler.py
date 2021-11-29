import os
import speech_recognition as sr
from pygame import *
from pynput import keyboard

class SpeechHandler:

    def __init__(self, directory):
        self.directory = directory
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.word = ""


    def speech_to_list(self):
        """

        Function is made to take microphone input and covert it into a list format
        for future text manipulation.

        """
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)

            print("Please say the sound file path: ")

            audio = self.r.listen(source)

            try:
                sound_path = str(self.r.recognize_google(audio))
                self.word = sound_path.replace(" ", "").lower()
                print(self.word)

                # self.word_list = self.word_list[0].split()
                # print(self.word_list)


            except Exception as e:
                print("Error: " + str(e))

    def play_song(self):
        """
        Function is meant to play a song from a file path verbally said in
        in speech_to_list function and queue them if needed
        """

        for filename in os.listdir(self.directory):
            f = os.path.join(self.directory, filename)
            if os.path.isfile(f):
                #print(f.endswith(self.word))
                print(f)
                if f.endswith(self.word):
                    print("OK")
                    mixer.init()
                    mixer.music.load(f)
                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                    while mixer.music.get_busy():
                        time.Clock().tick(10)

    def stop_song(self):
        mixer.music.stop()

def main():
    # mixer.init()
    # mixer.music.load(r"D:\Downloads\zapsplat_animals_dog_medium_sized_single_bark_slight_distance_001_70616.mp3")
    # mixer.music.set_volume(0.7)
    # mixer.music.play()
    #
    # while mixer.music.get_busy():
    #     time.Clock().tick(10)

    #playsound(r"D:\Downloads\zapsplat_animals_dog_medium_sized_single_bark_slight_distance_001_70616.mp3")
    sh = SpeechHandler(r'\Users\Chris\PycharmProjects\mytest_project\Music2')
    #C:\Users\Chris\PycharmProjects\mytest_project\Music
    sh.speech_to_list()
    sh.play_song()


if __name__ == "__main__":
    main()
