
#TASK 3

class Shop:
    def __init__(self):
        self.items = {
            'item1': 50,
            'item2': 120,
            'item3': 80,
            'item4': 150
        }
        self.available_money = 100
        self.purchase_attempts = 0

    def welcome_customer(self):
        print("Welcome to the shop!")
        print("Here are the available items and their prices:")
        for item, price in self.items.items():
            print(f"{item}: £{price}")
        print("To exit, enter 'exit'.")

    def process_purchase(self, option):
        if option == 'exit':
            raise ValueError("Exit selected.")
        if option not in self.items:
            raise ValueError("Invalid item selected.")

        price = self.items[option]
        if price > self.available_money:
            raise ValueError("Insufficient funds.")

        print(f"Here's your {option}!")
        self.available_money -= price

    def ask_for_more_money(self):
        more_money = input("Do you have more money? (Enter amount or 'no'): ")
        if more_money == 'no':
            print("Thank you for visiting the shop!")
        else:
            try:
                additional_money = int(more_money)
                self.available_money += additional_money
            except ValueError:
                print("Invalid amount entered. Exiting the shop.")

    def run_shop(self):
        self.welcome_customer()

        while self.purchase_attempts < 3:
            try:
                option = input("Enter the item you want to purchase (or 'exit' to leave): ")
                self.process_purchase(option)
            except ValueError as err:
                print(f"Error: {err}")
                self.ask_for_more_money()
                self.purchase_attempts += 1
            else:
                self.purchase_attempts += 1

        if self.purchase_attempts == 3:
            print("Maximum purchase attempts reached. Exiting the shop.")
