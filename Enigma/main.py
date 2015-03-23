from EnigmaMachine import EnigmaMachine

def main():
    e = EnigmaMachine()
    output = e.ProcessMessage('HELLOWORLD')    
    e.ResetMachine()
    output2 = e.ProcessMessage(output)
    
    e.ResetMachine()    

    output = e.ProcessMessage('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')
    e.ResetMachine()
    output2 = e.ProcessMessage(output)    
    
    e.ResetMachine()    
    
    long_output = e.ProcessMessage('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')   
    e.ResetMachine()
    long_output2 = e.ProcessMessage(long_output)

    print()
    print('Done...')
    print() 

main()