# Thanks to the following pages for the information and education I needed.
# http://red-badger.com/blog/2015/02/23/understanding-the-enigma-machine-with-30-lines-of-ruby-star-of-the-2014-film-the-imitation-game/
# http://en.wikipedia.org/wiki/Enigma_machine
# http://en.wikipedia.org/wiki/Enigma_rotor_details

# Version 1 - 3/23/2015
#   * Basic Enigma functionality; can encrypt/decrypt messages and set/reset rotor states
#   * Random plugboard configuration generated for each newly created EnigmaMachine object; not configurable at this time
#   * Only supports 3 rotors
#   * Does not support double-stepping of second rotor
#   * Limited configuration options for rotors and reflector
#   * Only supports English alphabet
#   * All messages are converted to upper-case

# Version 2 - 3/23/2015
#   * Added ability to configure plugboard manually or generate a random plugboard mapping
#   * Better plugboard error handling
#   * Added ability to set specific rotor positions
#   * Added machine-level methods that call component-level methods
#   * Print statements, conforming to Python's naming conventions, etc.

from Plugboard import Plugboard
from Rotors import Rotors
from Reflector import Reflector

class EnigmaMachine:
    def __init__(self):
        self._plugboard = Plugboard()
        self._rotors = Rotors()
        self._reflector = Reflector()    

    def set_rotor_position(self, rotor_num, rotor_position):
        print('Setting rotor ' + str(rotor_num) + ' to position ' + str(rotor_position))
        self._rotors.set_rotor_position(rotor_num, rotor_position)

    def add_plugboard_mapping(self, char1, char2):
        print('Adding plugboard mapping [' + char1.upper() + ' <-> ' + char2.upper() + ']')
        self._plugboard.add_mapping(char1, char2)

    def generate_random_plugboard_mapping(self):
        print('Generating random plugboard mappings...')
        self._plugboard.generate_random_mappings()

    def print_plugboard(self):
        self._plugboard.print()

    def reset_plugboard(self):
        print()
        print('Resetting plugboard...')
        print()
        self._plugboard.reset()

    def reset_rotors(self):
        print()
        print('Resetting rotors...')
        print()
        self._rotors.reset()  
        
    def reset_machine(self):
        print()
        print('Resetting machine (plugboard and rotor settings)...')
        print()
        self._plugboard.reset()
        self._rotors.reset()      

    def process_message(self, message):
        output = ''
        message = message.upper()
        for char in message:
            char = self._plugboard.input_letter(char)
            char = self._rotors.input_letter(char)
            char = self._reflector.reflect_letter(char)
            char = self._rotors.output_letter(char)
            char = self._plugboard.output_letter(char)

            output = output + char

            self._rotors.rotate()

        print('Original message: ' + message)
        print('Processed message: ' + output)
        return output