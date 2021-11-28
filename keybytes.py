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

class SoundBoard():
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
        if not os.path.exists('%skeybinds.txt' % self.dpath):
            f = open('%skeybinds.txt' % self.dpath, 'x')
            f.close()
        if not os.path.exists('%sSounds\\' % self.dpath):
            os.makedirs('%sSounds\\' % self.dpath)

    #Creates and saves keybyte based on user inputted keybind and sound file location
    def create_keybyte(self):
        print('\n\nCreate a Keybyte:')
        temp_soundbyte = ''
        temp_keybind = ''
        notIn = False

        #Error handling and input
        while not notIn:
            temp_keybind = input('Type the keys, separated by a plus, that you would like to assign a soundbyte to: ')
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

        parts = []
        parts = temp_soundbyte.split('\\')
        nAddress = '%sSounds\\%2s' % (self.dpath, parts[-1])
        shutil.copyfile(temp_soundbyte, nAddress)

        #Add keybyte to dictionary
        self.keybytes[temp_keybind] = nAddress

        #Add keybyte to file
        f = open('%skeybinds.txt' % self.dpath, 'a')
        f.write('%s, %s\n' % (temp_keybind, nAddress))
        f.close()
        print('\nKeybyte successfully created!')
        self.menu()

    #Loads keybytes from file into dictionary
    def load_keybytes(self):
        #Open file and prepare variables
        f = open('%skeybinds.txt' % self.dpath, 'r')
        lines = f.readlines()
        parts = []

        #Read through and append keybytes from file into dictionary
        if len(lines) > 0 and len(lines[0]) > 1:
            for line in lines:
                templine = line.strip()
                parts = templine.split(', ')
                self.keybytes[parts[0]] = parts[1]
                print('Added %s keybind, with %s file location' % (parts[0], parts[1]))
        f.close()

    #Lists all keybytes
    def list_keybytes(self):
        print('\n\nList Keybytes:')
        
        for line in self.keybytes:
            print('\nKeybind: %s' % line)
            print('Plays Sound: %s' % self.keybytes[line])

        self.menu()

    #Deletes keybyte based on user inputted keybind
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

            del self.keybytes[u_inpt]
            print('Successfully deleted Keybyte binded to: %s' % u_inpt)
        else:
            print('You currently have no Keybytes to delete.')

        self.menu()

    #Menu of soundboard
    def menu(self):
        u_inpt = None
        print('\n\n[1]: Create Keybyte')
        print('[2]: List Keybytes')
        print('[3]: Delete Keybyte')
        print('[4]: Exit Program')

        while not (u_inpt == '1' or u_inpt == '2' or u_inpt == '3' or u_inpt == '4'):
            u_inpt = input('\nPlease enter a number as shown above: ')
            if not (u_inpt == '1' or u_inpt == '2' or u_inpt == '3' or u_inpt == '4'):
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
        
#TODO Need to somehow constantly listen to the keyboard so that no matter what the user is doing, they can use their keybytes.

#Create soundboard instance and ensure that if the folder doesnt already exist it is created
sBoard = SoundBoard('%s\\KeyBytes\\' %  os.environ['APPDATA'] )
print('Welcome to Keybytes.')
sBoard.dirCheck()
sBoard.load_keybytes()
sBoard.menu()
