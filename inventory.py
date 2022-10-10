class Inventory:
    def __init__(self, name, weight_in_kg, price_per_kg):
        self.name = name
        self.weight_in_kg = weight_in_kg
        self.price_per_kg = price_per_kg

    def list_of_inventory(self):
        print(f'Item name : {self.name}')
        print(f'Item quantity : {self.weight_in_kg}')
        print(f'Price per KG : {self.price_per_kg}')

    def total_price(self):
        return self.price_per_kg * self.weight_in_kg


if __name__ == '__main__':
    inventory1 = Inventory("Rice", 10, 50)
    inventory1.list_of_inventory()
    print(f'Total price of {inventory1.name} :', inventory1.total_price())
    print("-------------------------")
    inventory2 = Inventory("Pulses", 20, 100)
    inventory2.list_of_inventory()
    print(f'Total price of {inventory2.name} :', inventory2.total_price())
    print("-------------------------")
    inventory3 = Inventory("Wheat", 30, 150)
    inventory3.list_of_inventory()
    print(f'Total price of {inventory3.name} : ', inventory3.total_price())
