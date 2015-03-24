import string

class Reflector:

    _alphabet = list(string.ascii_uppercase)

    def __init__(self):
        self._cipher_r = list('EJMZALYXVBWFCRQUONTSPIKHGD')      # Reflector A cipher
        # self.cipher_r = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')    # Reflector B cipher    

    def reflect_letter(self, char):
        index = self._cipher_r.index(char)
        return self._alphabet[index]