import unittest
import math_rg  


class TestBasicMath(unittest.TestCase):

    # --- square() ---
    def test_square_happy_path(self):
        self.assertEqual(math_rg.square(5), 25)   
        self.assertEqual(math_rg.square(-3), 9)   

    def test_square_edge_case(self):
        self.assertEqual(math_rg.square(0), 0)    

    # --- factorial() ---
    def test_factorial_happy_path(self):
        self.assertEqual(math_rg.factorial(5), 120) 
        self.assertEqual(math_rg.factorial(0), 1)   

    def test_factorial_error_case(self):
        with self.assertRaises(ValueError):
            math_rg.factorial(-1)

    # --- is_prime() ---
    def test_is_prime_happy_path(self):
        self.assertTrue(math_rg.is_prime(29))   
        self.assertTrue(math_rg.is_prime(2))    

    def test_is_prime_not_prime(self):
        self.assertFalse(math_rg.is_prime(1))   
        self.assertFalse(math_rg.is_prime(9))   

    # --- gcd() ---
    def test_gcd_happy_path(self):
        self.assertEqual(math_rg.gcd(24, 36), 12)  
        self.assertEqual(math_rg.gcd(17, 5), 1)    

    def test_gcd_edge_case(self):
        self.assertEqual(math_rg.gcd(0, 5), 5)     

    # --- lcm() ---
    def test_lcm_happy_path(self):
        self.assertEqual(math_rg.lcm(4, 6), 12)
        self.assertEqual(math_rg.lcm(21, 6), 42)

    def test_lcm_edge_case(self):
        self.assertEqual(math_rg.lcm(0, 7), 0)    


if __name__ == '__main__':
    unittest.main()
