import string
from EnigmaLogger import EnigmaLogger

class _Rotor:

    _alphabet = list(string.ascii_uppercase)

    def __init__(self, rotor_label, cipher_string, notch_windows, ringstellung = 'A', grundstellung = 'A', verbose = True):
        self._rotor_label = rotor_label
        if type(ringstellung) is str:
            self._ringstellung = ringstellung.upper()
        else:
            self._ringstellung = self.pos_to_alphabet_char(ringstellung)
        self._grundstellung = grundstellung.upper()
        self._notch_windows = notch_windows
        self._cipher_d = list(cipher_string)
        self._logger = EnigmaLogger(verbose)

    def char_to_alphabet_pos(self, char):
        return self._alphabet.index(char)

    def char_to_cipher_pos(self, char):
        return self._cipher_d.index(char)        

    def pos_to_alphabet_char(self, pos):
        return self._alphabet[pos % len(self._alphabet)]

    def pos_to_cipher_char(self, pos):
        return self._cipher_d[pos % len(self._cipher_d)]

    def set_ringstellung(self, pos):
        if type(pos) is str:
            self._ringstellung = pos.upper()
        else:
            self._ringstellung = self.pos_to_alphabet_char(pos)

    def set_grundstellung(self, pos):
        if type(pos) is str:
            self._grundstellung = pos.upper()
        else:
            self._grundstellung = self.pos_to_alphabet_char(pos)

    def rotate(self):
        rotate_next_rotor = any(self._grundstellung == notch_window.upper() for notch_window in self._notch_windows)

        self._logger.Log('Rotor ' + self._rotor_label + ' is rotating.')
        self._grundstellung = self.pos_to_alphabet_char(self.char_to_alphabet_pos(self._grundstellung) + 1)

        return rotate_next_rotor        

    def map_letter(self, char, reverse = False):
        position = self.char_to_alphabet_pos(char)
        position = (position + self.char_to_alphabet_pos(self._grundstellung) + len(self._alphabet) - self.char_to_alphabet_pos(self._ringstellung)) % len(self._alphabet)
        mapped_char = self.pos_to_alphabet_char(position)

        if reverse == True:
            position = self.char_to_cipher_pos(mapped_char)
            mapped_char = self.pos_to_alphabet_char(position)            
        else:
            mapped_char = self.pos_to_cipher_char(position)

        position = self.char_to_alphabet_pos(mapped_char)
        position = (position + ((len(self._alphabet) - self.char_to_alphabet_pos(self._grundstellung) + self.char_to_alphabet_pos(self._ringstellung))) % len(self._alphabet))
        
        mapped_char = self.pos_to_alphabet_char(position)
        return mapped_char   

    
       
        


