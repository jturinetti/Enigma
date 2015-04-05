from Rotor import _Rotor

class Rotors:
    ROTOR_I_CIPHER = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'      # rotor I cipher via the 1930 Enigma I
    ROTOR_II_CIPHER = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'     # rotor II cipher via the 1930 Enigma I
    ROTOR_III_CIPHER = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'    # rotor III cipher via the 1930 Enigma I

    def __init__(self, rotor_order = None):
        self.rotors = []
        if rotor_order is None:
            self.rotors.append(_Rotor(self.ROTOR_I_CIPHER))    
            self.rotors.append(_Rotor(self.ROTOR_II_CIPHER))    
            self.rotors.append(_Rotor(self.ROTOR_III_CIPHER))
        else:
            # TODO: this needs to be better
            for rotor_num in rotor_order:
                if rotor_num == 0:
                    self.rotors.append(_Rotor(self.ROTOR_I_CIPHER))
                elif rotor_num == 1:
                    self.rotors.append(_Rotor(self.ROTOR_II_CIPHER))    
                elif rotor_num == 2:
                    self.rotors.append(_Rotor(self.ROTOR_III_CIPHER))
                else:
                    # should throw error
                    pass

    def set_ring_position(self, rotor_num, starting_position):
        self.rotors[rotor_num]._position = starting_position % 26    

    def set_message_key(self, message_key):
        rotor_counter = 0
        for char in message_key:    # length of key should match # of rotors!
            #self.rotors[rotor_counter].set_rotor_offset(char)
            rotor_counter = rotor_counter + 1        

    def reset(self):        
        self.set_ring_position(0, 0)
        self.set_ring_position(1, 0)
        self.set_ring_position(2, 0)
        #self.rotors[0].reset_rotor_offset()
        #self.rotors[1].reset_rotor_offset()
        #self.rotors[2].reset_rotor_offset()

    def rotate(self):
        self.rotors[2].rotate()        
        if self.rotors[2].get_ring_position() == 0:
            self.rotors[1].rotate()
            if self.rotors[1].get_ring_position() == 0:
                self.rotors[0].rotate()

    def input_letter(self, char):
        for rotor in reversed(self.rotors):            
            char = rotor.input_letter(char)

        return char

    def output_letter(self, char):
        for rotor in self.rotors:
            char = rotor.output_letter(char)

        return char


