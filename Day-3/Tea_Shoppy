from abc import ABC, abstractmethod

# Abstract Base Class
class Chai(ABC):
    def __init__(self, name, base_price, quantity_in_stock):
        self.name = name
        self.base_price = base_price
        self.quantity_in_stock = quantity_in_stock

    @abstractmethod
    def calculate_price(self):
        """Calculate final price with additional cost."""
        pass

    @abstractmethod
    def display_info(self):
        """Display chai details."""
        pass


# Subclasses of Chai
class MasalaChai(Chai):
    def calculate_price(self):
        return self.base_price + 10  # Adding ₹10 spice cost

    def display_info(self):
        print(f"Name: {self.name} | Price per cup: ₹{self.calculate_price()} | Stock: {self.quantity_in_stock}")


class GingerChai(Chai):
    def calculate_price(self):
        return self.base_price + 8  # Adding ₹8 ginger cost

    def display_info(self):
        print(f"Name: {self.name} | Price per cup: ₹{self.calculate_price()} | Stock: {self.quantity_in_stock}")


class ElaichiChai(Chai):
    def calculate_price(self):
        return self.base_price + 12  # Adding ₹12 elaichi cost

    def display_info(self):
        print(f"Name: {self.name} | Price per cup: ₹{self.calculate_price()} | Stock: {self.quantity_in_stock}")


# Inventory Management Class
class ChaiInventory:
    def __init__(self):
        self.chai_list = []

    def add_chai(self, chai_obj):
        self.chai_list.append(chai_obj)

    def show_inventory(self):
        for chai in self.chai_list:
            chai.display_info()

    def get_total_inventory_value(self):
        total_value = sum(chai.calculate_price() * chai.quantity_in_stock for chai in self.chai_list)
        return total_value


# Sample Test Code
if __name__ == "__main__":
    inventory = ChaiInventory()

    chai1 = MasalaChai("Masala Chai", 20, 50)
    chai2 = GingerChai("Ginger Chai", 18, 40)
    chai3 = ElaichiChai("Elaichi Chai", 25, 30)

    inventory.add_chai(chai1)
    inventory.add_chai(chai2)
    inventory.add_chai(chai3)

    inventory.show_inventory()
    print("Total Inventory Value: ₹", inventory.get_total_inventory_value())
