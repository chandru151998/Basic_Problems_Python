class Stock:
    def __init__(self, name, share_quantity, share_price):
        self.name = name
        self.share_quantity = share_quantity
        self.share_price = share_price

    def list(self):
        print(f'Share name : {self.name}')
        print(f'Share quantity : {self.share_quantity}')
        print(f'Price of one share : {self.share_price}')

    def total_price(self):
        return self.share_price * self.share_quantity


if __name__ == '__main__':
    stock1 = Stock("SBIN", 1000, 600)
    stock1.list()
    print(f'Total share price of {stock1.name} :', stock1.total_price())
    print("-------------------------")
    stock2 = Stock("Infosys", 1200, 1200)
    stock2.list()
    print(f'Total share price of {stock2.name} :', stock2.total_price())
    print("-------------------------")
    stock3 = Stock("Zomato", 500, 80)
    stock3.list()
    print(f'Total share price of {stock3.name} : ', stock3.total_price())
    