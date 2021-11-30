# Names: Christopher Rossi, Paige Broussard, and Josh Degazio
# Project: Keybytes - voice activated soundboard
# Description: Keybytes is a school group project for CP317 (Software Enginnering)
#              and it is a voice activated soundboard to help handicapped individuals
#              play their favorite sound clips to their friends!
# Start Date: 11-05-2021
# End Date: ??/l
# Keybyte = the composite of keybind andsoundbyte
# Keybind = button(s) pressed in succession that do something (in this case play a soundbyte)
# Soundbyte = short audio clip that is usually funny, reactionary, or relatable.
import os
import sys
import shutil
from pygame import *
from pynput import keyboard
import threading
from EventHandler import *

class SoundBoard():
    keybytes = {}
    keywords = {}


    def __init__(self, dpath):
        self.dpath = dpath
        self.current = ''
        # self.keybytes = {}
        #self.thread3 = thread3


    # Creates folder in Appdata/Roaming, if one does not already exist, to store soundbytes.
    def dirCheck(self):
        # If it doesn't exist, create folder
        if not os.path.exists(self.dpath):
            os.makedirs(self.dpath)
            os.makedirs('%sSounds\\' % self.dpath)
            f = open('%skeybinds.txt' % self.dpath, 'x')
            f.close
            f = open('%skeywords.txt' % self.dpath, 'x')
            f.close
            # Create all other files we need here.
        if not os.path.exists('%skeybinds.txt' % self.dpath):
            f = open('%skeybinds.txt' % self.dpath, 'x')
            f.close()
        if not os.path.exists('%skeywords.txt' % self.dpath):
            f = open('%skeywords.txt' % self.dpath, 'x')
            f.close()
        if not os.path.exists('%sSounds\\' % self.dpath):
            os.makedirs('%sSounds\\' % self.dpath)

    # Creates and saves keybyte based on user inputted keybind and sound file location
    def create_keybyte(self):
        print('\n\nCreate a Keybyte:')
        temp_soundbyte = ''
        temp_keybind = ''
        temp_keyword = ''
        notIn = False
        notIn2 = False

        # Error handling and input
        while not notIn:
            temp_keybind = input('Type the key(s), without any spaces, that you would like to assign a soundbyte to: ')
            if temp_keybind in self.keybytes:
                print('You have entered a pre-existing keybind. Please try again.')
            elif temp_keybind == '':
                print('You have not entered a keybind. Please try again')
            else:
                notIn = True

        while not temp_soundbyte[-4:] == ('.mp3'):
            temp_soundbyte = input('Now enter the address of the mp3 file you wish to use as a soundbyte: ')
            if not temp_soundbyte.endswith('.mp3'):
                print('You have entered an incorrect file address for an mp3 file. Please try again.')

        while not notIn2:
            temp_keyword = input('Type the word(s), with spaces, that you would like to assign a soundbyte to for voice activation: ')
            if temp_keyword in self.keywords:
                print('You have entered a pre-existing keyword. Please try again.')
            elif temp_keyword == '':
                print('You have not entered a keyword. Please try again')
            else:
                notIn2 = True

        parts = []
        parts = temp_soundbyte.split('\\')
        nAddress = '%sSounds\\%2s' % (self.dpath, parts[-1])
        shutil.copyfile(temp_soundbyte, nAddress)

        # Add keybyte to dictionary
        self.keybytes[temp_keybind] = nAddress
        self.keywords[temp_keyword] = temp_keybind

        # Add keybyte to file
        f = open('%skeybinds.txt' % self.dpath, 'a')
        f.write('%s, %s\n' % (temp_keybind, nAddress))
        f.close()
        f = open('%skeywords.txt' % self.dpath, 'a')
        f.write('%s, %s\n' % (temp_keyword, temp_keybind))
        f.close()
        print('\nKeybyte successfully created!')
        self.menu()

    # Loads keybytes from file into dictionary
    def load_keybytes(self):
        # Open file and prepare variables
        f = open('%skeybinds.txt' % self.dpath, 'r')
        lines = f.readlines()
        parts = []

        # Read through and append keybytes from file into dictionary
        if len(lines) > 0 and len(lines[0]) > 1:
            for line in lines:
                templine = line.strip()
                parts = templine.split(', ')
                self.keybytes[parts[0]] = parts[1]
                print('Added %s keybind, with %s file location' % (parts[0], parts[1]))
        f.close()

        f = open('%skeywords.txt' % self.dpath, 'r')
        lines = f.readlines()
        parts = []

        # Read through and append keybytes from file into dictionary
        if len(lines) > 0 and len(lines[0]) > 1:
            for line in lines:
                templine = line.strip()
                parts = templine.split(', ')
                self.keywords[parts[0]] = parts[1]
                print('Added %s keyword, with %s keybind' % (parts[0], parts[1]))
        f.close()

    # Lists all keybytes
    def list_keybytes(self):
        print('\n\nList Keybytes:')

        for line in self.keybytes:
            print('\nKeybind: %s' % line)
            print('Plays Sound: %s' % self.keybytes[line])

        for line in self.keywords:
            print('\nKeyword: %s' % line)
            print('Plays keybind: %s' % self.keywords[line])

        self.menu()

    # Deletes keybyte based on user inputted keybind
    def delete_keybyte(self):
        if len(self.keybytes) > 0:
            print('\n\nDelete Keybyte:')
            u_inpt = ''
            notIn = False

            while not notIn:
                u_inpt = input('Enter the keybind of a Keybyte you wish to delete: ')
                if not u_inpt in self.keybytes:
                    print('Please enter an existing keybind.')
                else:
                    notIn = True

            with open('%skeybinds.txt' % self.dpath, 'r') as f:
                lines = f.readlines()
            with open('%skeybinds.txt' % self.dpath, 'w') as f:
                for line in lines:
                    tempParts = []
                    tempParts = (line.strip("\n")).split(', ')
                    if tempParts[0] != u_inpt:
                        f.write(line)
            with open('%skeywords.txt' % self.dpath, 'r') as f:
                lines = f.readlines()
            with open('%skeywords.txt' % self.dpath, 'w') as f:
                for line in lines:
                    tempParts = []
                    tempParts = (line.strip("\n")).split(', ')
                    if tempParts[1] != u_inpt:
                        f.write(line)

            os.remove(self.keybytes[u_inpt])
            del self.keybytes[u_inpt]
            del self.keywords[u_inpt]
            print('Successfully deleted Keybyte binded to: %s' % u_inpt)
        else:
            print('You currently have no Keybytes to delete.')

        self.menu()

    def check_voice(self):
        #print(self.keybytes)
        #print(self.keywords)
        sh = SpeechHandler
        l = sh.speech_to_list(self)
        #print(l)
        for i in range(len(l)):
            tempString = ''
            for j in range(i, len(l)):
                #print("nope1")
                tempString = tempString+ " " + l[j]
                tempString = tempString.strip()
                #print(tempString)
                if tempString in self.keywords:
                    #print("nope2")
                    self.play(self.keywords[tempString])



    def play(self, keybind):
        mixer.init()
        mixer.music.load(self.keybytes[keybind])
        mixer.music.set_volume(0.9)
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(10)

    def on_press(self, key):
        self.current = self.current + str(key)
        self.current = self.current.replace("'","")
        if self.current in self.keybytes:
            self.play(self.current)
        if str(key) == "'`'":
            thread3 = threading.Thread(target=self.check_voice(), args=())
            thread3.start()
            sh = menu
            sh.print_menu(self)

    # def push_talk(self, key):
    #     listener = keyboard.Listener(on_press=self.on_press)
    #     listener.start()
    #     if key == '`':
    #         thread3 = threading.Thread(target=sBoard.check_voice(), args=())
    #         thread3.start()


    # Play sound sBoard.keybytes[current]

    def on_release(self, key):
        try:
            self.current = "" #self.current[:(len(self.current) - 1)]
        except KeyError:
            pass

    def listen(self):

        # with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
        #     listener.start()
        #     print("n")
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release, suppress=False)
        listener.start()

    # Menu of soundboard
    def menu(self):
        u_inpt = None
        print('\n\n[1]: Create Keybyte')
        print('[2]: List Keybytes')
        print('[3]: Delete Keybyte')
        print('[`]: Toggle Speech-To-Play')
        print('[4]: Exit Program')

        while not (u_inpt == '1' or u_inpt == '2' or u_inpt == '3' or u_inpt == '4' or u_inpt == '5'):
            u_inpt = input('\nPlease enter a number as shown above: ')
            if not (u_inpt == '1' or u_inpt == '2' or u_inpt == '3' or u_inpt == '4' or u_inpt == '5'):
                print('Invalid input, please try again.')
                print(u_inpt)

        if u_inpt == '1':
            self.create_keybyte()
        elif u_inpt == '2':
            self.list_keybytes()
        elif u_inpt == '3':
            self.delete_keybyte()
        elif u_inpt == '4':
            sys.exit()
        elif u_inpt == '5':
            self.print_menu()


# TODO Need to somehow constantly listen to the keyboard so that no matter what the user is doing, they can use their keybytes.

# Create soundboard instance and ensure that if the folder doesnt already exist it is created
#thread3 = threading.Thread(target=sBoard.check_voice(), args=())
sBoard = SoundBoard('%s\\KeyBytes\\' % os.environ['APPDATA'])


print('Welcome to Keybytes.')
sBoard.dirCheck()
sBoard.load_keybytes()

thread1 = threading.Thread(target=sBoard.listen(), args=())
thread2 = threading.Thread(target=sBoard.menu(), args=())

thread1.start()
thread2.start()
#thread3.start()




# listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys

# with keyboard.Listener(on_press=sBoard.on_press, on_release=sBoard.on_release) as listener:
#     listener.join()
#     print("n")

# listener = keyboard.Listener(on_press=sBoard.on_press, on_release=sBoard.on_release)
# listener.start()  # start to listen on a separate thread
#sBoard.menu()
