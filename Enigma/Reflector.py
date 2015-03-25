import string

# umkehrwalze
class Reflector:

    _alphabet = list(string.ascii_uppercase)
    _REFLECTOR_A = 'EJMZALYXVBWFCRQUONTSPIKHGD'  # Reflector A cipher
    _REFLECTOR_B = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'  # Reflector B cipher

    def __init__(self, reflector = 'A'):
        if reflector == 'B':
            self._cipher_r = list(self._REFLECTOR_B)
        else:
            self._cipher_r = list(self._REFLECTOR_A)        

    def reflect_letter(self, char):
        index = self._cipher_r.index(char)
        return self._alphabet[index]