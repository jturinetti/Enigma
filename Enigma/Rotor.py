import string

class _Rotor(object):

    _alphabet = list(string.ascii_uppercase)

    def __init__(self, cipher_string, starting_position = 0):
        self._position = starting_position % 26
        #self._offset_position = 0
        self._cipher_d = list(cipher_string)  

    def rotate(self):
        self._position = (self._position + 1) % 26
        #self._offset_position = (self._offset_position + 1) % 26  # not sure if this is right...
        
    def set_ring_position(self, rotor_position):
         self._position = rotor_position % 26

    def get_ring_position(self):
        return self._position

    #def set_rotor_offset(self, char):
    #    char = char.upper()
    #    offset_counter = 0
    #    isFound = False
    #    while isFound == False:
    #        if char == self._alphabet[offset_counter]:
    #            self._offset_position = offset_counter
    #            isFound = True
    #        offset_counter = offset_counter + 1

    #def reset_rotor_offset(self):
    #    self._offset_position = 0

    def input_letter(self, char):
        index = self._alphabet.index(char)
        cipher_letter = self._cipher_d[((index + self._position) % 26)]
        return cipher_letter

    def output_letter(self, char):        
        #index = self._cipher_d.index(char)
        #alpha_letter =  self._alphabet[((index + self._position) % 26)]
        #return alpha_letter
        index = self._alphabet.index(char)
        cipher_letter = self._cipher_d[((index + self._position) % 26)]
        return cipher_letter
       
        


