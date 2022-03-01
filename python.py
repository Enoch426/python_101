# ENOCH'S SHAMPOO PROJECT


class Shampoo: #adding a class called Shampoo

    def __init__(self, inputted_brand, inputted_use, inputted_quantity, inputted_amount): #adding 4 variables: Brand, Use, How many, and How much.
        self.brand = inputted_brand 
        self.use = inputted_use
        self.quantity = inputted_quantity
        self.amount = inputted_amount

    def brand_(self):                           #shortcut to find product "brand"
        print("This Product is called: " + self.brand)

    def use_(self):                              #shortcut to get product "use" for
        print("Product Best used for: " + self.use) 

    def quantity_(self):                           #shortcut to the "stock" of the product
        print ("How much the product has in stock: " + str(self.quantity))

    def amount_(self):                              #shortcut to get to "price" or amount
        print("How much the Product is ", + str(self.amount))

    def all_(self):                                 #shortcut to print all four variable at once 
        print("\n\n" + self.brand + "\n\n " + self.use + "\n\n " + str(self.quantity) + "\n\n" + str(self.amount) + "\n\n")
