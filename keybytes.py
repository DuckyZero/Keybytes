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

class SoundBoard():
    #TODO Need to update this dictionary based on keybinds text file on startup.
    keybytes = {}

    def __init__(self, dpath):
        self.dpath = dpath
    
    #Creates folder in Appdata/Roaming, if one does not already exist, to store soundbytes.
    def dirCheck(self):
        #If it doesn't exist, create folder
        if not os.path.exists(self.dpath):
            os.makedirs(self.dpath)
            os.makedirs('%sSounds\\' % self.dpath)
            f = open('%skeybinds.txt' % self.dpath, 'x')
            f.close
            #Create all other files we need here.

    def create_keybyte(self):
        temp_keybind = input('Type the keys, separated by a plus, that you would like to assign a soundbyte to: ')
        temp_soundbyte = None

        while not temp_soundbyte.endswith('.mp3'):
            temp_soundbyte = input('Now enter the address of the mp3 file you wish to use as a soundbyte: ')
            if not temp_soundbyte.endswith('.mp3'):
                print('You have entered an incorrect file address for an mp3 file. Please try again.')

        self.keybytes[temp_keybind] = temp_soundbyte
        #TODO Add keybyte to keybinds text file


#TODO Need to somehow constantly listen to the keyboard so that no matter what the user is doing, they can use their keybytes.

#Create soundboard instance and ensure that if the folder doesnt already exist it is created
sBoard = SoundBoard('%s\\KeyBytes\\' %  os.environ['APPDATA'] )
sBoard.dirCheck()
