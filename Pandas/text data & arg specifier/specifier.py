# %s is used for strinng
product_cat = ["A", "B"]
# print("we have all 50 items in product category '%s'" %product_cat)

# %d is used for digits(integers)
product_num = [150, 250]
# print("we have all %d items in product category '%s'" %(product_num, product_cat ))

# %f is used for float(decima)
product_price = [2.60, 3.50]
# print("product '%s' costs just $%.2f" %(product_cat, product_price))
# the .2 befor the f signifies 2 decima place

i = 1

print("All products in '%s' should be sold at $%.2f so far the numbers are %d" %(product_cat[i], product_price[i], product_num[i]))

