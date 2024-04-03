import unittest

from final import KeyValue, dict2, CustomException

class TestDict2(unittest.TestCase):
    
    def test_setitem(self):
        obj = dict2()
        obj['a'] = 1
        self.assertEqual(obj['a'], 1)

    def test_getitem(self):
        obj = dict2()
        obj['a'] = 1
        val = obj['a']
        self.assertEqual(val,1)
    
    def test_custom_exception(self):
        try:
            raise CustomException("test_key")
        except CustomException as e:
            self.assertTrue(isinstance(e, Exception))
            self.assertEqual(str(e),f"ERROR occured key '{'test_key'}' not found")

    def test_iter(self):
        obj = dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3

        expected_result = ['a','b','c']
        actual_result = list(obj)

        self.assertEqual(actual_result, expected_result)



if __name__=="__main__":
    unittest.main()