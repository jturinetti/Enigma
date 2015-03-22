from Plugboard import Plugboard

def main():
    p = Plugboard()

    print(p.InputLetter('h'))
    print(p.InputLetter('i'))

    print(p.OutputLetter('h'))
    print(p.OutputLetter('i'))

    p.print()


main()