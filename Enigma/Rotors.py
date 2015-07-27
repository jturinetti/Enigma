from Rotor import _Rotor

class Rotors:
    ROTOR_I_CIPHER = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'      # rotor I cipher via the 1930 Enigma I
    ROTOR_II_CIPHER = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'     # rotor II cipher via the 1930 Enigma I
    ROTOR_III_CIPHER = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'    # rotor III cipher via the 1930 Enigma I
    ROTOR_IV_CIPHER = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'     # rotor IV cipher via the M3 Army Enigma
    ROTOR_V_CIPHER = 'VZBRGITYUPSDNHLXAWMJQOFECK'      # rotor V cipher via the M3 Army Enigma
    ROTOR_VI_CIPHER = 'JPGVOUMFYQBENHZRDKASXLICTW'     # rotor VI cipher via the M3 & M4 Naval Enigma
    ROTOR_VII_CIPHER = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'    # rotor VII cipher via the M3 & M4 Naval Enigma
    ROTOR_VIII_CIPHER = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'   # rotor VIII cipher via the M3 & M4 Naval Enigma

    def __init__(self, rotor_order = ['I', 'II', 'III'], ringstellung = ['A', 'A', 'A'], grundstellung = ['A', 'A', 'A'], verbose = True):
        self.rotors = []
        index = 0
        for rotor_num in rotor_order:
            uc_rotor_num = rotor_num.upper()
            if uc_rotor_num == 'I':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_I_CIPHER, ['Q'], ringstellung[index], grundstellung[index], verbose))
            elif uc_rotor_num == 'II':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_II_CIPHER, ['E'], ringstellung[index], grundstellung[index], verbose))    
            elif uc_rotor_num == 'III':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_III_CIPHER, ['V'], ringstellung[index], grundstellung[index], verbose))
            elif uc_rotor_num == 'IV':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_IV_CIPHER, ['J'], ringstellung[index], grundstellung[index], verbose))
            elif uc_rotor_num == 'V':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_V_CIPHER, ['Z'], ringstellung[index], grundstellung[index], verbose))
            elif uc_rotor_num == 'VI':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_VI_CIPHER, ['Z', 'M'], ringstellung[index], grundstellung[index], verbose))
            elif uc_rotor_num == 'VII':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_VII_CIPHER, ['Z', 'M'], ringstellung[index], grundstellung[index], verbose))
            elif uc_rotor_num == 'VIII':
                self.rotors.append(_Rotor(uc_rotor_num, self.ROTOR_VIII_CIPHER, ['Z', 'M'], ringstellung[index], grundstellung[index], verbose))
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


