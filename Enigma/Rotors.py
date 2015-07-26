from Rotor import _Rotor

class Rotors:
    ROTOR_I_CIPHER = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'      # rotor I cipher via the 1930 Enigma I
    ROTOR_II_CIPHER = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'     # rotor II cipher via the 1930 Enigma I
    ROTOR_III_CIPHER = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'    # rotor III cipher via the 1930 Enigma I

    def __init__(self, rotor_order = ['I', 'II', 'III'], ringstellung = ['A', 'A', 'A'], grundstellung = ['A', 'A', 'A'], verbose = True):
        self.rotors = []
        index = 0        
        for rotor_num in rotor_order:
            if rotor_num.upper() == 'I':
                self.rotors.append(_Rotor('I', self.ROTOR_I_CIPHER, 'Q', ringstellung[index], grundstellung[index], verbose))
            elif rotor_num.upper() == 'II':
                self.rotors.append(_Rotor('II', self.ROTOR_II_CIPHER, 'E', ringstellung[index], grundstellung[index], verbose))    
            elif rotor_num.upper() == 'III':
                self.rotors.append(_Rotor('III', self.ROTOR_III_CIPHER, 'V', ringstellung[index], grundstellung[index], verbose))
            else:
                # should throw error
                pass

            index = index + 1

    def input_letter(self, char):
        for rotor in reversed(self.rotors):                        
            char = rotor.map_letter(char)

        return char

    def output_letter(self, char):
        for rotor in self.rotors:            
            char = rotor.map_letter(char, True)

        return char

    def rotate(self):        
        index = len(self.rotors) - 1
        shouldContinue = True
        while shouldContinue == True and index >= 0:
            shouldContinue = self.rotors[index].rotate()
            index = index - 1

    def set_ringstellung(self, rotor_label, pos):
        for rotor in self.rotors:
            if rotor._rotor_label == rotor_label:
                rotor.set_ringstellung(pos)

    def set_grundstellung(self, rotor_label, pos):
        for rotor in self.rotors:
            if rotor._rotor_label == rotor_label:
                rotor.set_grundstellung(pos)


