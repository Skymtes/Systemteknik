from random import random, randrange
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from root.blending import Blend

class BlendingTest(unittest.TestCase):

    def test_blending_eanx36(self):
            mix = Blend(0.36, 0.0, 175, 0.16, 0.40, 45)
            expected_oxygen = 31.3
            expected_helium = 0
            expected_air = 98.7
            self.assertEqual(mix, (expected_oxygen, expected_helium, expected_air))
    def test_blending_eanx32(self):
            mix = Blend(0.36, 0.0, 175, 0.16, 0.40, 45)
            expected_oxygen = 31.3
            expected_helium = 0
            expected_air = 98.7
            self.assertEqual(mix, (expected_oxygen, expected_helium, expected_air))  
    def test_blending_eanx46(self):
            mix = Blend(0.36, 0.0, 175, 0.16, 0.40, 45)
            expected_oxygen = 31.3
            expected_helium = 0
            expected_air = 98.7
            self.assertEqual(mix, (expected_oxygen, expected_helium, expected_air))        
    def test_blending_zero_values(self):
            mix = Blend(0.0, 0.0, 0, 0, 0, 0)
            self.assertEqual(mix, "Can not by devied by zero")
    def test_missing_arguments(self):
            mix = Blend(0.0, 175, 0.16, 0.40, 45)
            self.assertEqual(mix,"Invaild input : missing arg")
    def test_string_input(self):
            mix = Blend(0.36, 0.0, "175", 0.16, 0.40, 45)
            self.assertEqual(mix,"Invaild input : input as str")
    def test_lower_pressure(self):
        mix = Blend(0.23, 0.08, 200, 0.35, 0.60, 50)
        self.assertEqual(mix,('Lower total pressure to: ', 26.6, 'Then fill with:', (0.4, 0.0, 173.0)))
    def test_range_input(self):
        test_num = randrange(300,500)
        idx = randrange(0,5)
        values = [900,9,158,90,40,287]
        values[idx] = test_num
        mix = Blend(*values)
        self.assertEqual(mix,"Invaild input : range limit")
    

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(BlendingTest)
    runner.run(suite)