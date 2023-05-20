import unittest
from translator import english_to_french, french_to_english

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english('None'), " ")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Hola')
                
class Testenglish_to_french(unittest.TestCase): 
    def test2(self): 
        self.assertNotEqual(english_to_french('None'), " ")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hola')


        
unittest.main()
