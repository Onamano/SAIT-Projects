# order_management.py

class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items  

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1] + item[2]  
        if total == 0:  
            return "Empty Order"
        return total

    def add_item(self, item_name, quantity, price)
        self.items.append((item_name, quantity, price))  

    def remove_item(self, item_name):
        for item in self.items:  
            if item[0] == item_name:
                self.items.remove(item)  

    def print_summary(self):
        print("Order Summary for", self.customer_name)
        for item in self.itemz: 
            print(f"{item[1]} x {item[0]} @ ${item[2]:.2f}")
        print("Total: $", self.calculate_total()

    def apply_discount(self, code): 
        if code == "SAVE10":
            return 0.1
        elif code == "SAVE20":
            return 0.2
        


def main():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.add_item("Notebook", 3, 5.00)
    order.remove_item("Pen")
    order.print_summary()
    discount = order.apply_discount("SAVE30")
    print("Discount rate:", discount)

main()
