from __future__ import print_function
from EnigmaMachine import EnigmaMachine

def run_tests():
    # e = EnigmaMachine([2, 1, 0])    # rotor order from left to right: III, II, I
    # e.set_rotor_ring_position(2, 25)
    # e.process_message('AAA')    
    
    # e.reset_machine()  

    e = EnigmaMachine(None, 'B')
    e.process_message('AAAAA')

    e.reset_machine()

    e.add_plugboard_mapping('a', 'z')
    e.add_plugboard_mapping('b', 'x')
    e.add_plugboard_mapping('d', 'd')
    e.add_plugboard_mapping('h', 'i')
    e.print_plugboard()

    output = e.process_message('HELLOWORLD') 
    e.reset_rotors()    
    output2 = e.process_message(output)
    
    e.reset_machine()   
    
    e.generate_random_plugboard_mapping() 
    e.print_plugboard()

    output = e.process_message('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')
    e.reset_rotors()
    output2 = e.process_message(output)    
    
    e.reset_machine()        
    
    e.set_rotor_ring_position(0, 25)
    e.set_rotor_ring_position(1, 25)
    e.set_rotor_ring_position(2, 10)
    e.set_rotor_offset('ABC')    

    long_output = e.process_message('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')   

    e.set_rotor_ring_position(0, 25)
    e.set_rotor_ring_position(1, 25)
    e.set_rotor_ring_position(2, 10)
    e.set_rotor_offset('ZZZ')

    # incorrect message key; this should be wrong
    wrong_output = e.process_message(long_output)

    # try again!
    e.set_rotor_ring_position(0, 25)
    e.set_rotor_ring_position(1, 25)
    e.set_rotor_ring_position(2, 10)
    e.set_rotor_offset('ABC')

    long_output2 = e.process_message(long_output)

    print()
    print('Done...')
    print() 

run_tests()