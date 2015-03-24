import string

class _Rotor(object):

    _alphabet = list(string.ascii_uppercase)

    def __init__(self, cipher_string, starting_position = 0):
        self._position = starting_position % 26  
        self._cipher_d = list(cipher_string)  

    def rotate(self):
        self._position = (self._position + 1) % 26       
        
    def set_position(self, rotor_position):
         self._position = rotor_position % 26

    def get_position(self):
        return self._position

    def input_letter(self, char):
        index = self._alphabet.index(char)
        return self._cipher_d[25 - ((index + self._position) % 26)]

    def output_letter(self, char):        
        index = self._cipher_d.index(char)
        return self._alphabet[25 - ((index + self._position) % 26)]
       
        


