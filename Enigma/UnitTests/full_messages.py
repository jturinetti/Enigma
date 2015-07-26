import unittest
from EnigmaMachine import EnigmaMachine

if __name__ == '__main__':
    unittest.main()

class full_messages(unittest.TestCase):
    # http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages#Enigma_Instruction_Manual.2C_1930
    def test_full_message_1(self):
        # create Enigma machine with initial settings
        e = EnigmaMachine(['II', 'I', 'III'], [23, 12, 21], ['A', 'B', 'L'], 'A')

        # add plugboard mappings
        e.add_plugboard_mapping('A', 'M')
        e.add_plugboard_mapping('F', 'I')
        e.add_plugboard_mapping('N', 'V')
        e.add_plugboard_mapping('P', 'S')
        e.add_plugboard_mapping('T', 'U')
        e.add_plugboard_mapping('W', 'Z')
         
        input_message = 'GCDSE AHUGW TQGRK VLFGX UCALX VYMIG MMNMF DXTGN VHVRM MEVOU YFZSL RHDRR XFJWC FHUHM UNZEF RDISI KBGPM YVXUZ'        

        decrypted_message = e.process_message(input_message)

        expected_message = 'FEIND LIQEI NFANT ERIEK OLONN EBEOB AQTET XANFA NGSUE DAUSG ANGBA ERWAL DEXEN DEDRE IKMOS TWAER TSNEU STADT'

        self.assertEqual(decrypted_message, expected_message)