from resto_data import *
from all_tasks import *
import argparse


class MainPage:
    def __init__(self):
        self.list_foods = []
        self.list_drinks = []
        self.list_services = []
        self.list_disc = []

    def details(self, a):
        print(a)
        print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
        print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")
        i = 0
        while i < len(self.list_foods) or i < len(self.list_drinks):
            var_space = 1
            if i <= 8:                   # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                var_space = 2
            if i < len(self.list_foods):
                food = " (" + str(i + 1) + ")" + " " * var_space + str(self.list_foods[i]) + "  | "  # Styling out the index number for the food or item and starting out from 1 for better human readability
            else:
                food = " " * 36 + "| "  # 36 is a constant for indention in console to fixup list in print
            if i < len(self.list_drinks):
                drink = "(" + str(41 + i) + ")" + " " + str(self.list_drinks[i]) 
            else:
                drink = ""
            print(food, drink)
            i += 1
        print("*" * 29 + "OTHER SERVICES" + "*" * 29)
        print(" |NO| |SERVICE NAME|      |PRICE|")  # Services Menu Structure

        i = 0
        while i < len(self.list_services):
            print(" (" + str(81 + i) + ")" + " " + str(self.list_services[i]))   # Services starts from 81 + and now it is being enumarated into a list.

            i += 1
        print("=====================================")
        pr = self.list_disc[:3]
        for i in range(len(self.list_disc)):
            if i > 2:
                print("Order your food and get", float(self.list_disc[i]) * 100, " % Off with Min. order Rs", pr[0])
                pr.pop(0)
        print("\n")
        print("If you would to order your food from this Restaurant?just enter")
        print("You wish to look out the prices on other Restauran?say yes!")
        take = input()
        if take:
            self.list_restaurant()
        s = Food(self.list_foods, self.list_drinks, self.list_services, self.list_disc, a)
        s.def_main()

    def list_of_foods_drinks(self):
        l = {"1": "Nagarjuna", "2": "A2B", "3": "shanthi", "4": "5star"}
        print("*" * 5 + "( If you wish to know the price of the food which you are looking for,\nplease enter the food and drink name )" + "*" * 5)
        print("\n")
        print("If you wish to go through the restaurant names and order your food, just enter")
        print("\n")
        new_food = input("Please enter the name of the food: ") 
        new_drink = input("Please enter the name of the drink: ")
        if new_food == "" and new_drink == "":
            self.list_restaurant()
        else:
            low_high_food = {}  # creating dictionary to store the food and price
            low_high_drink = {}  # creating dictionary to store the drink and price
            for key, val in l.items():
                a = Database_(key)  # creating instance of Database_ to fetch data from database
                item1, item2 = a.food_name_wise1(new_food, new_drink)
                if len(item1) == 0:
                    item1 = "Not found"
                if len(item2) == 0:
                    item2 = "Not found"
                low_high_food.update({val: item1})  # updating food and rink prices to dictionary
                low_high_drink.update({val: item2})
            print()
            print("*" * 10 + "FOOD" + "*" * 10)
            for k, v in low_high_food.items():
                print(k, "    :   ", v)
            print("*" * 10 + "DRINKS" + "*" * 10)
            for k2, v2 in low_high_drink.items():
                print(k2, "    :   ", v2)
            print("* " * 25)
            print("\n")
            print("If you wish to give a look on other food..please say yes!")
            print("If you wish to order this food, just enter")
            print()
            print("* " * 25)
            input__ = input("yes or no")
            if input__ != "":
                self.list_of_foods_drinks()
            else:
                self.list_restaurant()

    def complete_information(self):                           # To fetch the food and drink based on RESTAURANT name.
        l = {"1": "Nagarjuna", "2": "A2B", "3": "shanthi", "4": "5star"}
        name_res = input("Please select the RESTAURANT..: ")

        if len(name_res) == 1:
            a = Database_(name_res)
            self.list_foods, self.list_drinks, self.list_services, self.list_disc = a.def_full_file_reader()
            self.details(l[name_res])
        else:
            print("Please enter the valid input")
            self.complete_information()

    def list_restaurant(self):
        print("You can go through the Restaurant Names and choose one!!")
        print("\n")
        print("*" * 31 + "RESTAURANT NAMES" + "*" * 32 + "\n\t(1) NAGARJUNA\n\t(2) A2B\n\t(3) SHANTI SAGAR\n\t(4) 5STAR\n" + "_" * 72)
        print("=====================================")
        self.complete_information()

    def main_page(self):
        print("\n\n\n")
        print("* " * 10 + "Welcome " + "* " * 20)
        print("\n")
        print("* " * 10 + "Great food awaits you!" + "* " * 13)
        print("\n")
        print("*" * 48)
        print("\n")
        print("As you stay in...Don't worry about takeout!")
        print(" " * 10 + "We are now delivering!!" + " " * 20)
        print("\n")
        print("*" * 48)
        print("\n")
        print("\n")
        self.list_of_foods_drinks()

    def update_menu(self, args):
        d_update = Database_(args.resName[0])
        foodToUpdate = input("enter food name and price to be updated")
        d_update.update_food(foodToUpdate)
        drinkToUpdate = input("enter drink name and price to be updated")
        d_update.update_drink(drinkToUpdate)
        print("updated")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = '''==================================Update food and drinks into menu==================================''') 
    parser.add_argument("--resName", type = str, nargs = 1, 
                        metavar = "rs_name", default = None, 
                        help = "RESTAURANT NAMES" + "\n"     

                        
                        "\t(1) NAGARJUNA\n"                              
                        "\t(2) A2B\n"
                        "\t(3) SHANTI SAGAR\n"
                        "\t(4) 5STAR\n")  # defining arguments for parser object 
    args = parser.parse_args()

    mP = MainPage()
    if args.resName != None:
        mP.update_menu(args)
    else:
        mP.main_page()  # python -m flake8 --ignore F403,E501,E741,E741,E251,W291,F405 main_file.py