from __future__ import print_function
import string
from random import shuffle

class Plugboard:

    _alphabet = list(string.ascii_uppercase)

    def __init__(self):        
        self.reset()
    
    def reset(self):
        self._plugboard = [None] * 26
        self._mapped_chars = []
        self._doesMappingExist = False

    def add_mapping(self, char1, char2):
        char1 = char1.upper()
        char2 = char2.upper()

        if char1 == char2:
            return        

        if char1 in self._mapped_chars or char2 in self._mapped_chars:
            print('Cannot map characters that are already mapped.')
            return

        if len(self._mapped_chars) == 20:   # 10 pairs of mapped characters
            print('Max number of plugboard mappings reached.')
            return

        index1 = self._alphabet.index(char1)
        index2 = self._alphabet.index(char2)
        self._plugboard[index2] = char1
        self._plugboard[index1] = char2
        self._fill()
        self._doesMappingExist = True
    
    def generate_random_mappings(self):
        self.reset()

        swapped_letters = list(string.ascii_uppercase)
        shuffle(swapped_letters)        
        swapped_letters = swapped_letters[0:20]                

        i = 0
        while i < len(swapped_letters):         
            char1 = swapped_letters[i]
            char2 = swapped_letters[i+1]
            index1 = self._alphabet.index(char1)
            index2 = self._alphabet.index(char2)
            self._plugboard[index2] = char1
            self._plugboard[index1] = char2
            i = i + 2
            self._mapped_chars.append(char1)
            self._mapped_chars.append(char2)

        self._fill()     
        self._doesMappingExist = True     
                    
    def print(self):
        print(self._plugboard)

    def input_letter(self, char):
        if self._doesMappingExist == False:
            return char

        alphabet_index = self._alphabet.index(char)
        return self._plugboard[alphabet_index]        

    def output_letter(self, char):
        if self._doesMappingExist == False:
            return char

        plugboard_index = self._plugboard.index(char)
        return self._alphabet[plugboard_index]
        
    def _fill(self):
        alphabet_counter = 0
        for char in self._alphabet:
            if self._plugboard[alphabet_counter] is None:
                self._plugboard[alphabet_counter] = char

            alphabet_counter = alphabet_counter + 1