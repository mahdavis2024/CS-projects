'''
<<<Control flow in Python>>>
A Python program to simulate a scenario of baking and eating cupcakes at a party
'''

# Class Initialization
class Cupcake:
    def __init__(self, flavor, topping):
        self.flavor = flavor
        self.topping = topping
    def how_many(self, number):
        print(" 1\n\tWe need {} {} cupcakes, with {} topping.".format(number,self.flavor,self.topping))
           
# Sequential Execution
welcome_statement = " 2\n\t*** Welcome to my cupcake Party ***"
print(welcome_statement.title())


# Loops + Nested
cupcake_flavors = ["Vanilla", "Strawberry", "Saffron", "Chocolate"]

for flavor in cupcake_flavors:
    print(" 3\n\tDo you like " + flavor + "?")
    
    if flavor == "Strawberry":
        print(" 4\n\tThe Strawberry cupcakes are everyone's favorite!")
    elif flavor == "Saffron":
        print(" 5\n\tYum, Saffron flavor, Persian!")
    else:
        print(" 6\n\tBaking " + flavor + " cupcakes.")

# Conditional Statements
baking_time = 22
#baking_time = input("Enter the required baking time: ")
if baking_time >= 30:
    print(" 7\n\tThe cupcakes are ready to be taken out of the oven.")
else:
    print(" 8\n\tThe cupcakes need more time to bake")

# Class Object
my_cake = Cupcake("Orange", "Honey Drizzle")
print(" 9\n\tMy choice - Flavor:", my_cake.flavor, "- Topping:", my_cake.topping)
your_cake = Cupcake("Saffron", "Sesame Seeds")
print(" 10\n\tYour choice - Flavor:", your_cake.flavor, "- Topping:", your_cake.topping)

your_cake.how_many(7)


# Jump Statements (Break and Continue)
cupcake_toppings = ["Ganache", "Cheese Frosting", "Buttercream", "Sesame Seeds"]
for topping in cupcake_toppings:
    if topping == "Ganache":
        continue
    if topping == "Buttercream":
        print(" 11\n\tFound the perfect topping:", topping)
        break
    else:
        print(" 12\n\tTrying out", topping)

# Function Calls
def eat_cupcake(cupcake):
    print(" 13\n\tEating a", cupcake.flavor, "cupcake with", cupcake.topping, "topping")

eat_cupcake(my_cake)

# Exception Handling
num_guests = -2
# num_guests = int(input("Enter the number of guests at the party: "))
try:  
    if num_guests <= 0:
        raise ValueError(" 14\n\tNumber of guests should be positive")
except ValueError as ve:
    print(" 15\n\tInvalid input:", ve)
else:
    print(" 16\n\tNumber of guests at the party:", num_guests)

finally:
    print(" 17\n\tBon appétit!")
