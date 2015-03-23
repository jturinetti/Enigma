from Plugboard import Plugboard
from Rotors import Rotors
from Reflector import Reflector

class EnigmaMachine:
    def __init__(self):
        self.plugboard = Plugboard()
        self.rotors = Rotors()
        self.reflector = Reflector()    

    def ProcessMessage(self, message):
        output = ''
        for char in message:
            char = self.plugboard.InputLetter(char)
            char = self.rotors.InputLetter(char)
            char = self.reflector.ReflectLetter(char)
            char = self.rotors.OutputLetter(char)
            char = self.plugboard.OutputLetter(char)

            output = output + char

            self.rotors.Rotate()

        print('Original message: ' + message)
        print('Processed message: ' + output)
        return output
    
    def ResetMachine(self):
        print('Resetting machine...')
        self.rotors.ResetRotors()
