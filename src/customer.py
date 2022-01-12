class Customer:
    def __init__(self, name, wallet, age, drunkenness_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = drunkenness_level

    def reduce_wallet(self, amount):
        self.wallet -= amount

    
    def increase_mad_with_it(self, amount):
        self.drunkenness_level += amount

    

    