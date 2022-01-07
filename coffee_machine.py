class CoffeeMachine:
    def __init__(self, water_amount = 400, milk_amount = 540, coffee_amount = 120, cups_amount = 9, money_amount = 550):
        self.water_amount = water_amount
        self.milk_amount = milk_amount
        self.coffee_amount = coffee_amount
        self.cups_amount = cups_amount
        self.money_amount = money_amount
        self.main()
    
    def __str__(self):
        print("The coffee machine has:")
        print(f"{self.water_amount} ml of water")
        print(f"{self.milk_amount} ml of milk")
        print(f"{self.coffee_amount} g of coffee beans")
        print(f"{self.cups_amount} of disposable cups")
        print(f"{self.money_amount} of money")

    def give_money(self):
        print(f"I gave you ${self.money_amount}")
        self.money_amount = 0
        
    def fill_machine(self):
        water_added = int(input("Write how many ml of water you want to add:"))
        self.water_amount += water_added
        milk_added = int(input("Write how many ml of milk you want to add: "))
        self.milk_amount += milk_added
        coffee_added = int(input("Write how many grams of coffee beans you want to add: "))
        self.coffee_amount += coffee_added
        cups_added = int(input("Write how many disposable coffee cups you want to add: "))
        self.cups_amount += cups_added

    def buy_action(self, answer):
        #  1 - espresso, 2 - latte, 3 - cappuccino
        ingredients_dict = {1: {'water': 250, 'milk': 0, 'coffee': 16, 'money': 4, 'cup': 1},
                            2: {'water': 350, 'milk': 75, 'coffee': 20, 'money': 7, 'cup': 1}, 
                            3: {'water': 200, 'milk': 100, 'coffee': 12, 'money': 6, 'cup': 1}}
        if (self.water_amount >= ingredients_dict[answer]['water'] 
                and self.milk_amount >= ingredients_dict[answer]['milk'] 
                and self.coffee_amount >= ingredients_dict[answer]['coffee'] 
                and self.cups_amount >= ingredients_dict[answer]['cup']):
            print("I have enough resources, making you a coffee!")
            self.water_amount -= ingredients_dict[answer]['water']
            self.milk_amount -= ingredients_dict[answer]['milk']
            self.coffee_amount -= ingredients_dict[answer]['coffee']
            self.money_amount += ingredients_dict[answer]['money']
            self.cups_amount -= ingredients_dict[answer]['cup']
        else:
            print("Sorry, not enough resources!")
    def main(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action == 'take':
                self.give_money()
                continue
            elif action == 'fill':
                self.fill_machine()
                continue
            elif action == 'buy':
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                answer = input()
                if answer == 'back':
                    continue
                else:
                    answer = int(answer)
                    if answer in [1, 2, 3]:
                        self.buy_action(answer)
                        continue
                    else:
                        print("Input correct values!")
                        continue
            elif action == 'remaining':
                self.__str__()
                continue
            elif action == 'exit':
                pass
                break

coffee_machine = CoffeeMachine()




    