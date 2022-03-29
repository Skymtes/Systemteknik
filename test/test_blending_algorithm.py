import unittest

from backend.algorithm.blending_algorithm import Blend

class BlendingTest(unittest.TestCase):
    def test_blending_eanx36(self):
        with self.subTest():
            mix = Blend(0.36, 0.0, 175, 0.16, 0.40, 45)

            expected_oxygen = 31.3
            expected_helium = 0
            expected_air = 98.7
            self.assertEqual(mix, (expected_oxygen, expected_helium, expected_air))

    def test_blending_zero_values(self):
        with self.subTest():
            mix = Blend(0.0, 0.0, 0, 0, 0, 0)

            # TODO: add assertion method

    def test_missing_arguments(self):
        self.assertRaises(TypeError, Blend)
