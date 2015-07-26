from EnigmaMachine import EnigmaMachine

def main():  
    # class for quick tests and stuff
    e = EnigmaMachine(['I', 'II', 'III'], ['B', 'B', 'B'], ['A', 'A', 'A'], 'B')
    output_message = e.process_message('AAAAA')

    e2 = EnigmaMachine(['I', 'II', 'III'], ['B', 'B', 'B'], ['A', 'A', 'A'], 'B')
    reverted_message = e2.process_message(output_message)

    e3 = EnigmaMachine()
    m1 = e3.process_message('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')
    e4 = EnigmaMachine()
    m2 = e4.process_message(m1)

main()