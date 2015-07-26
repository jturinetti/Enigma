import unittest
from EnigmaMachine import EnigmaMachine

if __name__ == '__main__':
    unittest.main()

class test_messages(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_offset
    def test_rotor_offset(self):
        input_message = 'AAAAA'
        em = EnigmaMachine(['I', 'II', 'III'], ['A', 'A', 'A'], ['A', 'A', 'A'], 'B', False)
        encrypted_message = em.process_message(input_message)
        em = EnigmaMachine(['I', 'II', 'III'], ['A', 'A', 'A'], ['A', 'A', 'A'], 'B', False)
        decrypted_message = em.process_message(encrypted_message)

        self.assertEqual(encrypted_message, 'BDZGO')
        self.assertEqual(input_message, decrypted_message)

    def test_rotor_offset_int_pos(self):
        input_message = 'AAAAA'
        em = EnigmaMachine(['I', 'II', 'III'], [0, 0, 0], ['A', 'A', 'A'], 'B', False)
        encrypted_message = em.process_message(input_message)
        em = EnigmaMachine(['I', 'II', 'III'], [0, 0, 0], ['A', 'A', 'A'], 'B', False)
        decrypted_message = em.process_message(encrypted_message)
        
        self.assertEqual(encrypted_message, 'BDZGO')
        self.assertEqual(input_message, decrypted_message)

    # https://en.wikipedia.org/wiki/Enigma_rotor_details#Ring_setting
    def test_ring_setting(self):
        input_message = 'AAAAA'
        em = EnigmaMachine(['I', 'II', 'III'], ['B', 'B', 'B'], ['A', 'A', 'A'], 'B', False)
        encrypted_message = em.process_message(input_message)
        em = EnigmaMachine(['I', 'II', 'III'], ['B', 'B', 'B'], ['A', 'A', 'A'], 'B', False)
        decrypted_message = em.process_message(encrypted_message)
        
        self.assertEqual(encrypted_message, 'EWTYX')
        self.assertEqual(input_message, decrypted_message)

    def test_ring_setting_int_pos(self):
        input_message = 'AAAAA'
        em = EnigmaMachine(['I', 'II', 'III'], [1, 1, 1], ['A', 'A', 'A'], 'B', False)
        encrypted_message = em.process_message(input_message)
        em = EnigmaMachine(['I', 'II', 'III'], [1, 1, 1], ['A', 'A', 'A'], 'B', False)
        decrypted_message = em.process_message(encrypted_message)
        
        self.assertEqual(encrypted_message, 'EWTYX')
        self.assertEqual(input_message, decrypted_message)

    def test_long_message(self):
        input_message = 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG'
        e = EnigmaMachine()
        encrypted_message = e.process_message(input_message)
        e = EnigmaMachine()
        decrypted_message = e.process_message(encrypted_message)

        self.assertEqual(input_message, decrypted_message)