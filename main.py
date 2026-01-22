from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee = CoffeeMaker()
machine = MoneyMachine()

machine_on = True
while machine_on:
    choice = input(f"What would you want ({menu.get_items()}) ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
         coffee.report()
         machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                coffee.make_coffee(drink)