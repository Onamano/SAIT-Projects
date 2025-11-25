import unittest
from Buggy_Code_fixed import Order

#Tests that add_item, remove_item, calculate_total, and apply_discount functions are working together.
class TestIntegration(unittest.TestCase):

    def test_calculate_total(self):
        order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
        order.add_item("Notebook", 3, 5.00)
        order.remove_item("Pen")
        total = order.calculate_total()
        self.assertEqual(total, 45.00)

    def test_apply_discount(self):
        order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
        
        discount = order.apply_discount(code="SAVE10")
        self.assertEqual(discount, 0.1)

        discount = order.apply_discount(code="SAVE20")
        self.assertEqual(discount, 0.2)
    
        discount = order.apply_discount(code="SAVE30")
        self.assertEqual(discount, 0.3)

if __name__ == "__main__":
    unittest.main()
