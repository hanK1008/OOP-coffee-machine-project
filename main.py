from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
money_management = MoneyMachine()



machine_on = True

while machine_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    user_drink = menu.find_drink(user_input)
    # user_drink_cost = user_drink.cost

    if user_input == 'report':
        coffee_machine.report()
        money_management.report()

    elif user_input == 'off':
        machine_on = False

    else:
        if coffee_machine.is_resource_sufficient(user_drink):
            if money_management.make_payment(user_drink.cost):
                coffee_machine.make_coffee(user_drink)















