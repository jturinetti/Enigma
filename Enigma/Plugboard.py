import string
from random import shuffle

class Plugboard(object):

    _alphabet = list(string.ascii_uppercase)

    def __init__(self):
        self.plugboard = [None] * 26        
        swapped_letters = list(string.ascii_uppercase)
        shuffle(swapped_letters)        
        swapped_letters = swapped_letters[0:20]

        alphabet_counter = 0
        swapped_letters_counter = 0                

        i = 0
        while i < len(swapped_letters):         
            char1 = swapped_letters[i]
            char2 = swapped_letters[i+1]
            index1 = self._alphabet.index(char1)
            index2 = self._alphabet.index(char2)
            self.plugboard[index2] = char1
            self.plugboard[index1] = char2
            i = i + 2

        for char in self._alphabet:
            if self.plugboard[alphabet_counter] is None:
                self.plugboard[alphabet_counter] = char

            alphabet_counter = alphabet_counter + 1            
            
    def print(self):
        print(self.plugboard)


    def InputLetter(self, char):
        alphabet_index = self._alphabet.index(char)
        return self.plugboard[alphabet_index]        

    def OutputLetter(self, char):
        plugboard_index = self.plugboard.index(char)
        return self._alphabet[plugboard_index]
        