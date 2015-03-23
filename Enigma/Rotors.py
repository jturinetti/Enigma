from Rotor import _Rotor

class Rotors(object):

    _rotor_I_cipher = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'      # rotor I cipher via the 1930 Enigma I
    _rotor_II_cipher = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'     # rotor II cipher via the 1930 Enigma I
    _rotor_III_cipher = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'    # rotor III cipher via the 1930 Enigma I

    def __init__(self):
        self.rotors = []
        self.rotors.append(_Rotor(self._rotor_I_cipher))    
        self.rotors.append(_Rotor(self._rotor_II_cipher))    
        self.rotors.append(_Rotor(self._rotor_III_cipher))    

    def SetRotorStartingPosition(self, rotor_num, starting_position):
        self.rotors[rotor_num].position = starting_position % 26

    def ResetRotors(self):        
        self.SetRotorStartingPosition(0, 0)
        self.SetRotorStartingPosition(1, 0)
        self.SetRotorStartingPosition(2, 0)

    def Rotate(self):
        self.rotors[0].Rotate()        
        if self.rotors[0].position == 0:
            self.rotors[1].Rotate()
            if self.rotors[1].position == 0:
                self.rotors[2].Rotate()

    def InputLetter(self, char):
        for rotor in self.rotors:
            char = rotor.InputLetter(char)

        return char

    def OutputLetter(self, char):
        for rotor in reversed(self.rotors):
            char = rotor.OutputLetter(char)

        return char


