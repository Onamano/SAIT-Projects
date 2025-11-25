import unittest
from Buggy_Code_fixed import Order, main

class IntegrationTest(unittest.TestCase):
    def test_main(self):
        instance = Order("Mike", [("Book", 3, 15.00), ("Notebook", 4, 5.00), ("Pen", 1, 1.50)])
        # instance = main()
        self.assertEqual(main(), "Mike", [("Book", 3, 15.00), ("Notebook", 7, 5.00)])

if __name__ == "__main__":
    unittest.main()