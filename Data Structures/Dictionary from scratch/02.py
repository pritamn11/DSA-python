import unittest

def multiply(a,b):
    return a*b



class TestStringMethods(unittest.TestCase):

    def check_str(self):
        self.assertEqual('foo'.upper(),'FOO')

    
    def test_str(self):
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        txt = 'hello world'
        self.assertEqual(txt.split(),['hello','world'])
        with self.assertRaises(TypeError):
            txt.split(5)

    def test_function(self):
        result = multiply(3,4)
        self.assertEqual(result,12)

if __name__=="__main__":
    unittest.main()



