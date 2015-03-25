from __future__ import print_function
from EnigmaMachine import EnigmaMachine

def main():    
    # e = EnigmaMachine([0, 1, 2], 'B')
    # e.set_rotor_offset('AAA')
    # e.process_message('AAAAA')

    e = EnigmaMachine([1, 0, 2], 'A')   # need to work on clarity of this constructor
    e.add_plugboard_mapping('a', 'm')
    e.add_plugboard_mapping('f', 'i')
    e.add_plugboard_mapping('n', 'v')
    e.add_plugboard_mapping('p', 's')
    e.add_plugboard_mapping('t', 'u')
    e.add_plugboard_mapping('w', 'z')   
    e.print_plugboard()

    e.set_rotor_ring_position(0, 23)     # position 24
    e.set_rotor_ring_position(1, 12)     # position 13
    e.set_rotor_ring_position(2, 21)     # position 22

    e.set_rotor_offset('ABL')

    # GCDSE AHUGW TQGRK VLFGX UCALX VYMIG MMNMF DXTGN VHVRM MEVOU YFZSL RHDRR XFJWC FHUHM UNZEF RDISI KBGPM YVXUZ
    e.process_message('GCDSEAHUGWTQGRKVLFGXUCALXVYMIGMMNMFDXTGNVHVRMMEVOUYFZSLRHDRRXFJWCFHUHMUNZEFRDISIKBGPMYVXUZ')

main()