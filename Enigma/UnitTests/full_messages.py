import unittest
from EnigmaMachine import EnigmaMachine

if __name__ == '__main__':
    unittest.main()

class full_messages(unittest.TestCase):
    # http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages#Enigma_Instruction_Manual.2C_1930
    def test_full_message_1(self):
        # create Enigma machine with initial settings
        e = EnigmaMachine(['II', 'I', 'III'], [23, 12, 21], ['A', 'B', 'L'], 'A', False)

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

    # http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages#Operation_Barbarossa.2C_1941
    def test_full_message_2(self):
        # create Enigma machine with initial settings
        e = EnigmaMachine(['II', 'IV', 'V'], [1, 20, 11], ['B', 'L', 'A'], 'B', False)

        # add plugboard mappings
        e.add_plugboard_mapping('A', 'V')
        e.add_plugboard_mapping('B', 'S')
        e.add_plugboard_mapping('C', 'G')
        e.add_plugboard_mapping('D', 'L')
        e.add_plugboard_mapping('F', 'U')
        e.add_plugboard_mapping('H', 'Z')
        e.add_plugboard_mapping('I', 'N')
        e.add_plugboard_mapping('K', 'M')
        e.add_plugboard_mapping('O', 'W')
        e.add_plugboard_mapping('R', 'X')
         
        input_message_1 = 'EDPUD NRGYS ZRCXN UYTPO MRMBO FKTBZ REZKM LXLVE FGUEY SIOZV EQMIK UBPMM YLKLT TDEIS MDICA GYKUA CTCDO MOHWX MUUIA UBSTS LRNBZ SZWNR FXWFY SSXJZ VIJHI DISHP RKLKA YUPAD TXQSP INQMA TLPIF SVKDA SCTAC DPBOP VHJK-'
        decrypted_message_1 = e.process_message(input_message_1)
        expected_message_1 = 'AUFKL XABTE ILUNG XVONX KURTI NOWAX KURTI NOWAX NORDW ESTLX SEBEZ XSEBE ZXUAF FLIEG ERSTR ASZER IQTUN GXDUB ROWKI XDUBR OWKIX OPOTS CHKAX OPOTS CHKAX UMXEI NSAQT DREIN ULLXU HRANG ETRET ENXAN GRIFF XINFX RGTX-'
        
        e.set_grundstellung('II', 'L')
        e.set_grundstellung('IV', 'S')
        e.set_grundstellung('V', 'D')

        input_message_2 = 'SFBWD NJUSE GQOBH KRTAR EEZMW KPPRB XOHDR OEQGB BGTQV PGVKB VVGBI MHUSZ YDAJQ IROAX SSSNR EHYGG RPISE ZBOVM QIEMM ZCYSG QDGRE RVBIL EKXYQ IRGIR QNRDN VRXCY YTNJR'
        decrypted_message_2 = e.process_message(input_message_2)
        expected_message_2 = 'DREIG EHTLA NGSAM ABERS IQERV ORWAE RTSXE INSSI EBENN ULLSE QSXUH RXROE MXEIN SXINF RGTXD REIXA UFFLI EGERS TRASZ EMITA NFANG XEINS SEQSX KMXKM XOSTW XKAME NECXK'

        self.assertEqual(decrypted_message_1, expected_message_1)
        self.assertEqual(decrypted_message_2, expected_message_2)
        
    # http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages#Scharnhorst_.28Konteradmiral_Erich_Bey.29.2C_1943
    def test_full_message_3(self):
        # create Enigma machine with initial settings
        e = EnigmaMachine(['III', 'VI', 'VIII'], [0, 7, 12], ['U', 'Z', 'V'], 'B', False)

        # add plugboard settings
        e.add_plugboard_mapping('A', 'N')
        e.add_plugboard_mapping('E', 'Z')
        e.add_plugboard_mapping('H', 'K')
        e.add_plugboard_mapping('I', 'J')
        e.add_plugboard_mapping('L', 'R')
        e.add_plugboard_mapping('M', 'Q')
        e.add_plugboard_mapping('O', 'T')
        e.add_plugboard_mapping('P', 'V')
        e.add_plugboard_mapping('S', 'W')
        e.add_plugboard_mapping('U', 'X')

        input_message = 'YKAE NZAP MSCH ZBFO CUVM RMDP YCOF HADZ IZME FXTH FLOL PZLF GGBO TGOX GRET DWTJ IQHL MXVJ WKZU ASTR'
        decrypted_message = e.process_message(input_message)
        expected_message = 'STEUE REJTA NAFJO RDJAN STAND ORTQU AAACC CVIER NEUNN EUNZW OFAHR TZWON ULSMX XSCHA RNHOR STHCO'

        self.assertEqual(decrypted_message, expected_message)