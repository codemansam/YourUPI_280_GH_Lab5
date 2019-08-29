import unittest     # Import the Python unit testing framework
import maths        # Our code to test
from logging import _loggerClass


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        '''Tests the add function'''
        result = maths.add(5, 7)
        self.assertEqual(12, result, "maths.add did not return the expected result")
        
    def test_add_with_convert_base(self):
        ''' Tests the maths.add function with a base converter ''' 
        result = maths.add(10, 11, 16)
        self.assertEqual(15, result, "maths.add with convert base did not return the expected result")    
        

    def test_fibonacci(self):
        ''' Tests the maths.fibonacci function'''
        result = maths.fibonacci(5)
        self.assertEqual(5, result, "maths.fibonacci did not return the expected result")
    
    def test_convert_base_under_base_10(self):
        ''' Tests the maths.convert_base function with a base under 10 '''
        result = maths.convert_base(15, 2)
        self.assertEqual(1111, result, "maths.convert_base did not return the expected result for a conversion to a base under 10")
        
    def test_convert_base_over_base_10(self):
        ''' Tests the mats.convert_base function with a base over 10 '''
        result = maths.convert_base(31,16)
        self.assertEqual("1F", result, "maths.convert_base did not return the expected result for a conversion to a base over 10")
    
    def test_fibonacci(self):
        result = maths.fibonacci(4)
        self.assertEqual(24, result)
        
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
