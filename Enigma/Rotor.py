import string
from collections import deque

class _Rotor(object):

    _alphabet = list(string.ascii_uppercase)

    def __init__(self, cipher_string, starting_position = 0):
        self.position = starting_position % 26     
        self.SetCipherString(cipher_string)           

    def SetCipherString(self, cipher_string):
        self.cipher_d = list(cipher_string)

    def Rotate(self):
        self.position = (self.position + 1) % 26        

    def InputLetter(self, char):
        index = self._alphabet.index(char)
        return self.cipher_d[25 - ((index + self.position) % 26)]

    def OutputLetter(self, char):        
        index = self.cipher_d.index(char)
        return self._alphabet[25 - ((index + self.position) % 26)]
       
        


