import lab1 as c
import unittest
 
class gcdTest(unittest.TestCase):
 
    def test_Gcd_1(self):
        result = c.gcd(10, 15)
        self.assertEqual(result, 5)

    def test_Gcd_2(self):
        result = c.gcd(35, 10)
        self.assertEqual(result, 5)    

    def test_gcd_3(self):
        result = c.gcd(31, 2)
        self.assertEqual(result, 1)  


 
 
if __name__ == '__main__':
    unittest.main()