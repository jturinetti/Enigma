# Enigma Machine Simulator

# Thanks to the following pages for the information and education I needed.
# http://red-badger.com/blog/2015/02/23/understanding-the-enigma-machine-with-30-lines-of-ruby-star-of-the-2014-film-the-imitation-game/
# http://en.wikipedia.org/wiki/Enigma_machine
# http://en.wikipedia.org/wiki/Enigma_rotor_details
# http://users.telenet.be/d.rijmenants/en/enigmatech.htm
# http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages
# http://enigma.louisedade.co.uk/help.html

# Version 1 - 3/23/2015
#   * Basic Enigma functionality; can encrypt/decrypt messages and set/reset rotor states
#   * Random plugboard configuration generated for each newly created EnigmaMachine object; not configurable at this time
#   * Only supports 3 rotors
#   * Does not support double-stepping rotors
#   * Limited configuration options for rotors and reflector
#   * Only supports English alphabet
#   * All messages are converted to upper-case

# Version 2 - 3/23/2015
#   * Added ability to configure plugboard manually or generate a random plugboard mapping
#   * Better plugboard error handling
#   * Added ability to set specific rotor positions
#   * Added machine-level methods that call component-level methods
#   * Print statements, conforming to Python's naming conventions, etc.

# Version 3 - 7/22/2015
#   * Fixed the machine. It be broke no more.
#   * Added print methods to show character mappings and rotor rotations.
#   * Allowed integers to be taken as arguments for initial ring positions in addition to letters.
#   * Added folder for unit tests and several unit tests / test shell classes.
#   * Added configurability around verboseness of logging.
#   * Added definitions in comments for those who cannot read German.
#   * Only supports rotors I, II, and III with hard-coded notch positions at this time.

# Version 4 - 7/28/2015
#   * Added support for additional rotors (rotors I through VIII now supported)
#   * Added more unit test shells
#   * Commented out failing test because of incorrect information on Wikipedia (?)

# Version 5 - 8/9/2015
#   * Updated unit test shells for invalid constructor args; will only focus on EnigmaMachine object parameters
#   * Added private validate method to check EnigmaMachine parameter types & values
#   * Added list of acceptable rotor & reflector values

from __future__ import print_function
import string
from Plugboard import Plugboard
from Reflector import Reflector
from Rotors import Rotors

class EnigmaMachine:

    _alphabet = list(string.ascii_uppercase)
    _valid_rotors = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
    _valid_reflectors = ['A', 'B']

    # walzenlage: rotor order
    # ringstellung: ring setting
    # grundstellung: ground setting / start position
    # umkehrwalze: reflector
    def __init__(self, walzenlage = ['I', 'II', 'III'], ringstellung = ['A', 'A', 'A'], grundstellung = ['A', 'A', 'A'], umkehrwalze = 'A', verbose = True):
        # validate machine parameters
        self.__validate__(walzenlage, ringstellung, grundstellung, umkehrwalze)

        # set variables for machine usage
        self._plugboard = Plugboard(verbose)
        self._rotors = Rotors(walzenlage, ringstellung, grundstellung, verbose)
        self._reflector = Reflector(umkehrwalze, verbose)
    
    def __validate__(self, walzenlage, ringstellung, grundstellung, umkehrwalze):
        # check parameter types
        assert isinstance(walzenlage, list)        
        assert isinstance(ringstellung, list)
        assert isinstance(grundstellung, list)
        assert type(umkehrwalze) is str

        # check parameter lengths        
        rotor_count = len(walzenlage)
        ringstellung_count = len(ringstellung)
        grundstellung_count = len(grundstellung)
        assert rotor_count == ringstellung_count == grundstellung_count
        assert len(umkehrwalze) == 1

        # check for invalid array values & types
        for rotor in walzenlage:
            assert type(rotor) is str            
            assert rotor.upper() in self._valid_rotors
        for r in ringstellung:
            assert type(r) is str
            assert len(r) == 1
            assert r.upper() in self._alphabet
        for g in grundstellung:
            assert type(g) is str
            assert len(g) == 1
            assert g.upper() in self._alphabet
        assert umkehrwalze.upper() in self._valid_reflectors

    # steckerbrett: plugboard
    def add_plugboard_mapping(self, char1, char2):        
        self._plugboard.add_mapping(char1, char2)

    def generate_random_plugboard_mapping(self):        
        self._plugboard.generate_random_mappings()
        self.print_plugboard()

    def print_plugboard(self):
        self._plugboard.print()

    def reset_plugboard(self):                
        self._plugboard.reset()    

    def set_ringstellung(self, rotor_label, pos):
        self._rotors.set_ringstellung(rotor_label, pos)

    def set_grundstellung(self, rotor_label, pos):
        self._rotors.set_grundstellung(rotor_label, pos)

    def process_message(self, message):
        output = ''
        message = message.upper()
        for char in message:

            if char in self._alphabet:
                # rotation occurs first
                self._rotors.rotate()
                
                char = self._plugboard.input_letter(char)
                char = self._rotors.input_letter(char)
                char = self._reflector.reflect_letter(char)
                char = self._rotors.output_letter(char)
                char = self._plugboard.output_letter(char)

                output = output + char
            else:
                output = output + char

        print()
        print('Original Message: ' + message)
        print('Processed Message: ' + output)
        print()
        return output