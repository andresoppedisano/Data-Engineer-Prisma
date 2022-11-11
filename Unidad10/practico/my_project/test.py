import imp


import unittest
import functions

class TestMyFunctions(unittest.TestCase):
    def test_convert_string_to_lower(self):
        self.assertEquals(functions.convert_string_to_lower('POO'), 'poo')



if __name__ == '__main__':
    unittest.main()