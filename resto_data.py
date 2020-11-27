class Database_:                                    # class to fetch the restaurant menu

    def __init__(self, n):                           # Initialise variables to fetch food,drink and services from database
        self.list_foods = []                          # to fetch list of foods
        self.list_drinks = []                         # To fetch list of drinks 
        self.list_services = []                       # To fetch services
        self.var_discount_ = []                     # First discount starts.
        if n == str(1):
            self.name = "nagarjuna"                   # file name to fetch the details
        if n == str(2):
            self.name = "A2B"                         # file name to fetch the details
        if n == str(3):
            self.name = "shanthi"                     # file name to fetch the details
        if n == str(4):
            self.name = "5Star"                       # file name to fetch the details

    def def_full_file_reader(self):                                                                     
        file_foods = open('database_file' + "\\" + self.name + "\\" + 'list_foods.fsd', 'r')  # Reading Food List
        for i in file_foods:  # Line by line reading
            self.list_foods.append(str(i.strip()))  # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
        file_foods.close()

        file_drinks = open('database_file' + "\\" + self.name + "\\" + 'list_drinks.fsd', 'r')  # Reading Drinks List
        for i in file_drinks:
            self.list_drinks.append(str(i.strip()))
        file_drinks.close()

        file_services = open('database_file' + "\\" + self.name + "\\" + 'list_services.fsd', 'r')  # Reading Services
        for i in file_services:
            self.list_services.append(str(i.strip()))
        file_services.close()

        file_discounts = open('database_file' + "\\" + self.name + "\\" + 'disc.fsd', 'r')
        for i in file_discounts:
            self.var_discount_.append(i)
        file_discounts.close()

        i = 0
        while i <= (len(self.list_foods) - 1):   # Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
            if 'Rs' in self.list_foods[i]:
                self.list_foods[i] = str(self.list_foods[i][:self.list_foods[i].index('Rs') - 1]) + ' ' * (20 - (self.list_foods[i].index('Rs') - 1)) + str(self.list_foods[i][self.list_foods[i].index('Rs'):])
            i += 1

        i = 0
        while i <= (len(self.list_drinks) - 1):
            if 'Rs' in self.list_drinks[i]:
                self.list_drinks[i] = str(self.list_drinks[i][:self.list_drinks[i].index('Rs') - 1]) + ' ' * (20 - (self.list_drinks[i].index('Rs') - 1)) + str(self.list_drinks[i][self.list_drinks[i].index('Rs'):])
            i += 1

        i = 0
        while i <= (len(self.list_services) - 1):
            if 'Rs' in self.list_services[i]:
                self.list_services[i] = str(self.list_services[i][:self.list_services[i].index('Rs') - 1]) + ' ' * (20 - (self.list_services[i].index('Rs') - 1)) + str(self.list_services[i][self.list_services[i].index('Rs'):])
            i += 1
        return (self.list_foods, self.list_drinks, self.list_services, self.var_discount_)

    def food_name_wise1(self, foo_name = "", drink_name = ""):                                                          
        file_foods = open('database_file' + "\\" + self.name + "\\" + 'list_foods.fsd', 'r')  # Reading Food List
        for i in file_foods: 
            if foo_name in i:  # Line by line reading
                self.list_foods.append(str(i.strip()))   # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
        file_foods.close()
        file_drinks = open('database_file' + "\\" + self.name + "\\" + 'list_drinks.fsd', 'r')  # Reading Drinks List
        for i in file_drinks:
            if drink_name in i:
                self.list_drinks.append(str(i.strip()))
        file_drinks.close()
        i = 0
        while i <= (len(self.list_foods) - 1):  # Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
            if 'Rs' in self.list_foods[i]:
                self.list_foods[i] = str(self.list_foods[i][:self.list_foods[i].index('Rs') - 1]) + ' ' * (20 - (self.list_foods[i].index('Rs') - 1)) + str(self.list_foods[i][self.list_foods[i].index('Rs'):])
            i += 1
        i = 0
        while i <= (len(self.list_drinks) - 1):
            if 'Rs' in self.list_drinks[i]:
                self.list_drinks[i] = str(self.list_drinks[i][:self.list_drinks[i].index('Rs') - 1]) + ' ' * (20 - (self.list_drinks[i].index('Rs') - 1)) + str(self.list_drinks[i][self.list_drinks[i].index('Rs'):])
            i += 1
        return (self.list_foods, self.list_drinks)

    def update_food(self, add_food):
        with open('database_file' + "\\" + self.name + "\\" + 'list_foods.fsd', 'a') as file_foods:  # Reading Food 
            file_foods.write("\n")
            file_foods.write(add_food)

    def update_drink(self, add_drink):
        with open('database_file' + "\\" + self.name + "\\" + 'list_drinks.fsd', 'a') as file_drinks:  # Reading Drinks List
            file_drinks.write("\n")
            file_drinks.write(add_drink)