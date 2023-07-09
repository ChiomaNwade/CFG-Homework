import unittest
from shop import Shop

class ShopTestCase(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()

    def test_valid_purchase(self):
        """Test a valid purchase by checking if the available money is updated correctly."""
        self.shop.process_purchase('item1')
        self.assertEqual(self.shop.available_money, 50)

    def test_invalid_item(self):
        """Test purchasing an invalid item raises a ValueError."""
        with self.assertRaises(ValueError):
            self.shop.process_purchase('item5')

    def test_insufficient_funds(self):
        """Test purchasing an item with insufficient funds raises a ValueError."""
        with self.assertRaises(ValueError):
            self.shop.process_purchase('item4')

    def test_ask_for_more_money(self):
        """Test adding more money to the available funds."""
        self.shop.ask_for_more_money()
        self.assertEqual(self.shop.available_money, 100)

    def test_maximum_purchase_attempts(self):
        """Test reaching the maximum purchase attempts and check if a ValueError is raised."""
        self.shop.purchase_attempts = 3
        with self.assertRaises(ValueError):
            self.shop.run_shop()


if __name__ == '__main__':
    unittest.main()
