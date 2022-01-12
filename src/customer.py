class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay_till(self, amount):
        self.wallet -= amount

    