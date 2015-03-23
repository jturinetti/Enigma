import string
from collections import deque

class _Rotor(object):

    _alphabet = list(string.ascii_uppercase)

    def __init__(self, cipher, starting_position = 0):
        self.position = starting_position % 26     
        self.SetCipherString(cipher)           

    def SetCipherString(self, cipher):
        self.cipher_d = deque(list(cipher))

    def Rotate(self):
        self.position = (self.position + 1) % 26
        self.cipher_d.rotate()

    def InputLetter(self, char):
        index = self._alphabet.index(char)
        return self.cipher_d[index]

    def OutputLetter(self, char):
        cd_list = list(self.cipher_d)
        index = cd_list.index(char)
        return self._alphabet[index]
       
        


