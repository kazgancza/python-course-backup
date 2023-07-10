from cart import *

phone1 = Phone("Phone X", 2000, "red")
tv1 = TV("TV Y", 5000, 55)

cart = Cart()
cart.add_product(phone1)
cart.add_product(tv1)
cart.add_product(tv1)
cart.add_product("test")
cart.calculate_cart()
print(cart)

