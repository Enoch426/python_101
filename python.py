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


s1 = Shampoo("Neutrogina", "Dry scalp", 22, 16.99)
s2 = Shampoo("Jupiter", "Dandruff", 23, 17.99)
s3 = Shampoo("Biotique Kelp Protien", "Falling hair", 24, 18.99)
s4 = Shampoo("shea", "Curly Hair", 25, 19.99)


s1.brand_(),s1.use_(),s1.quantity_(),s1.amount_(), # s1.all_()

