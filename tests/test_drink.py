import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Blue Dragon", 1000.00)

    def test_drink_has_name(self):
        self.assertEqual("Blue Dragon", self.drink.name)

    

    