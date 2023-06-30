#TASK 4
# Unit Tests
import unittest


class ShopTestCase(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()

    def test_valid_purchase(self):
        self.shop.process_purchase('item1')
        self.assertEqual(self.shop.available_money, 50)

    def test_invalid_item(self):
        with self.assertRaises(ValueError):
            self.shop.process_purchase('item5')

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.shop.process_purchase('item4')

    def test_ask_for_more_money(self):
        self.shop.ask_for_more_money()
        self.assertEqual(self.shop.available_money, 100)

    def test_maximum_purchase_attempts(self):
        self.shop.purchase_attempts = 3
        with self.assertRaises(ValueError):
            self.shop.process_purchase('item1')


if __name__ == '__main__':
    unittest.main()



