import unittest
from Buggy_Code_fixed import Order

# Testing the calulate_total function in Buggy Code.py
class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        instance = Order("Mike", [("Book", 3, 15.00), ("Notebook", 4, 5.00)])
        self.assertEqual(instance.calculate_total(), 65.00)

# Testing the discount code matching the discount amount in Buggy_Code_fixed.py
class TestDiscount(unittest.TestCase):
    def test_add_discount(self):
        instance = Order.apply_discount(self, code="SAVE10")
        self.assertEqual(instance, 0.1)

        instance = Order.apply_discount(self, code="SAVE20")
        self.assertEqual(instance, 0.2)
    
        instance = Order.apply_discount(self, code="SAVE30")
        self.assertEqual(instance, 0.3)

if __name__ == "__main__":
    unittest.main()





# References
# [1] https://www.geeksforgeeks.org/python/unit-testing-python-unittest/ - Unit Test Guide
# [2] https://coderivers.org/blog/python-integration-testing/ - Integration Test guide