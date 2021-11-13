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

class soundBoard():
    #Need a keybind global string array that gets loaded into the program on startup from a file.


    def create_keybyte():
        tempKeybind = input("Type the keys, seperated by a plus, that you would like to assign a soundbyte to: ")
        tempSoundbyte = None

        while tempSoundbyte.endswith(".mp3") == False:
            tempSoundbyte = input("Now enter the address of the mp3 file you wish to use as a soundbyte: ")
            if tempSoundbyte.endswith(".mp3") == False:
                print("You have entered an incorrect file address to an mp3 file. Please try again.")
        #save_keybyte(tempSoundbyte, tempKeybind)
        
    def save_keybyte(tempSoundbyte, tempKeybind):
        #Save keybyte to file so it can be loaded on startup
        #and potentially save the soundbyte itself to a folder for easier access.

    #Need to somehow constantly listen to the keyboard so that no matter what the user is doing, they can use their keybytes.
