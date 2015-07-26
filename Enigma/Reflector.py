import string
from EnigmaLogger import EnigmaLogger

# umkehrwalze
class Reflector:

    _alphabet = list(string.ascii_uppercase)
    _REFLECTOR_A = 'EJMZALYXVBWFCRQUONTSPIKHGD'  # Reflector A cipher
    _REFLECTOR_B = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'  # Reflector B cipher

    def __init__(self, reflector = 'A', verbose = True):
        self._logger = EnigmaLogger(verbose)
        self._reflector_label = reflector.upper()
        if self._reflector_label == 'B':
            self._cipher_r = list(self._REFLECTOR_B)
        else:
            self._cipher_r = list(self._REFLECTOR_A)        

    def reflect_letter(self, char):
        input_char = char
        index = self._cipher_r.index(char)
        output_char = self._alphabet[index]

        self._logger.Log('Reflector ' + self._reflector_label + ': ' + input_char.upper() + ' -> ' + output_char.upper())

        return output_char