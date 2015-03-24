import string

class _Rotor(object):

    _alphabet = list(string.ascii_uppercase)

    def __init__(self, cipher_string, starting_position = 0):
        self._position = starting_position % 26
        self._message_key_position = 0
        self._cipher_d = list(cipher_string)  

    def rotate(self):
        self._position = (self._position + 1) % 26       
        
    def set_ring_position(self, rotor_position):
         self._position = rotor_position % 26

    def get_ring_position(self):
        return self._position

    def set_rotor_offset(self, char):
        char = char.upper()
        offset_counter = 0
        isFound = False
        while isFound == False:
            if char == self._cipher_d[offset_counter]:
                self._message_key_position = offset_counter
                isFound = True
            offset_counter = offset_counter + 1

    def reset_rotor_offset(self):
        self._message_key_position = 0

    def input_letter(self, char):
        index = self._alphabet.index(char)
        return self._cipher_d[25 - ((index + self._position + self._message_key_position) % 26)]

    def output_letter(self, char):        
        index = self._cipher_d.index(char)
        return self._alphabet[25 - ((index + self._position + self._message_key_position) % 26)]
       
        


