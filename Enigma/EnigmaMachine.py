# Thanks to the following pages for the information and education I needed.
# http://red-badger.com/blog/2015/02/23/understanding-the-enigma-machine-with-30-lines-of-ruby-star-of-the-2014-film-the-imitation-game/
# http://en.wikipedia.org/wiki/Enigma_machine
# http://en.wikipedia.org/wiki/Enigma_rotor_details

# Version 1 - 3/23/2015
# Basic Enigma functionality
#   * Random plugboard configuration generated for each newly created EnigmaMachine object; not configurable at this time
#   * Only supports 3 rotors
#   * Does not support double-stepping of second rotor
#   * Limited configuration options for rotors and reflector
#   * Only supports English alphabet
#   * All messages are converted to upper-case

from Plugboard import Plugboard
from Rotors import Rotors
from Reflector import Reflector

class EnigmaMachine:
    def __init__(self):
        self.plugboard = Plugboard()
        self.rotors = Rotors()
        self.reflector = Reflector()    

    def ProcessMessage(self, message):
        output = ''
        message = message.upper()
        for char in message:
            char = self.plugboard.InputLetter(char)
            char = self.rotors.InputLetter(char)
            char = self.reflector.ReflectLetter(char)
            char = self.rotors.OutputLetter(char)
            char = self.plugboard.OutputLetter(char)

            output = output + char

            self.rotors.Rotate()

        print('Original message: ' + message)
        print('Processed message: ' + output)
        return output
    
    def ResetMachine(self):
        print()
        print('Resetting machine...')
        print()
        self.rotors.ResetRotors()
