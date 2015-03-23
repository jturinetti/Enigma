from EnigmaMachine import EnigmaMachine

def main():
    e = EnigmaMachine()
    output = e.ProcessMessage('HELLOWORLD')
    e.ResetMachine()
    output2 = e.ProcessMessage(output)

    print()
    e.ResetMachine()
    print()

    output = e.ProcessMessage('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')
    e.ResetMachine()
    output2 = e.ProcessMessage(output)    

main()