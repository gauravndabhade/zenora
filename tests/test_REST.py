import unittest

class testTesting(unittest.TestCase):


    def setUp(self):
        self.username = "frog"
        self.age = 5
    
    def test_addition(self):
        self.assertEqual(self.age,5)



if __name__ == '__main__':
    unittest.main()