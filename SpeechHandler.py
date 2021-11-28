import os
from playsound import playsound
import speech_recognition as sr
from multiprocessing import Queue


class SpeechHandler:

    def __init__(self, directory):
        self.directory = directory
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.word = ""
        # When you want to queue multiple sound files
        self.queue = Queue()

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
        self.word = "amongus.wav"

        for filename in os.listdir(self.directory):
            f = os.path.join(self.directory, filename)
            if os.path.isfile(f):
                #print(f.endswith(self.word))
                print(f)
                if f.endswith(self.word):
                    print("OK")
                    playsound(f)



    def stop_song(self):
        pass

    def queue_song(self):
        pass


def main():
    import pygame

    pygame.mixer.init()
    my_sound = pygame.mixer.Sound(r'C:\Users\Chris\PycharmProjects\mytest_project\Music\amongus.ogg')
    my_sound.play()
    pygame.time.wait(int(my_sound.get_length() * 1000))
    #sh = SpeechHandler(r'\Users\Chris\PycharmProjects\mytest_project\Music')
    #C:\Users\Chris\PycharmProjects\mytest_project\Music
    #sh.speech_to_list()
    #sh.play_song()


if __name__ == "__main__":
    main()
