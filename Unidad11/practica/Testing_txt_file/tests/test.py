import sys
import datetime
import unittest


class MyTests(unittest.TestCase):
    def test_hola(self):

        to_check = 'Hola'
        valid_word = 'Hola'
        self.assertEqual(valid_word, to_check)
    
    def test_fruit_is_in(self):

        to_check = ['Banana', 'Manzana', 'Frutilla']
        valid_word = 'Frutilla'
        self.assertIn(valid_word, to_check)


#  insert_header() nos agrega el título, la fecha y la hora en la que se ejecutó el tests.

def insert_header(f):
    f.write('\n')
    f.write('******************TESTING**************************')
    f.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f.write(date_time)
    f.write('\n')
    return f


# main() se ocupa de generar un test suit con los test cases, los ejecuta y guarda los resultados en el archivo testing.txt.

def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
if __name__ == '__main__':
    with open('testing.txt', 'a') as f:
        f = insert_header(f)
        main(f)