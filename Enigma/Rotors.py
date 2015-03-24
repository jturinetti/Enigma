from Rotor import _Rotor

class Rotors:
    ROTOR_I_CIPHER = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'      # rotor I cipher via the 1930 Enigma I
    ROTOR_II_CIPHER = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'     # rotor II cipher via the 1930 Enigma I
    ROTOR_III_CIPHER = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'    # rotor III cipher via the 1930 Enigma I

    def __init__(self):
        self.rotors = []
        self.rotors.append(_Rotor(self.ROTOR_I_CIPHER))    
        self.rotors.append(_Rotor(self.ROTOR_II_CIPHER))    
        self.rotors.append(_Rotor(self.ROTOR_III_CIPHER))    

    def set_rotor_position(self, rotor_num, starting_position):
        self.rotors[rotor_num]._position = starting_position % 26

    def reset(self):        
        self.set_rotor_position(0, 0)
        self.set_rotor_position(1, 0)
        self.set_rotor_position(2, 0)

    def rotate(self):
        self.rotors[0].rotate()        
        if self.rotors[0].get_position() == 0:
            self.rotors[1].rotate()
            if self.rotors[1].get_position() == 0:
                self.rotors[2].rotate()

    def input_letter(self, char):
        for rotor in self.rotors:
            char = rotor.input_letter(char)

        return char

    def output_letter(self, char):
        for rotor in reversed(self.rotors):
            char = rotor.output_letter(char)

        return char


