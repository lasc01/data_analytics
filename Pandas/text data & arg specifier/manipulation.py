car_shop = ['Fast Cars', 'Elegant Cars']
car_brand = ['Audi', 'Ford']
number_of_cars_for_sale = [1000, 1200]
price_of_model = 37500.50
# \n takes next value to a new line
print('Current list of local car shops:\n"%s"\n"%s"' %(car_shop[0],car_shop[1]))

# \r is the carriage return
print("Product A1 is our best category of products. \rCategory A")

car_shop = ['Fast Cars', 'Elegant Cars']
car_brand = ['Audi', 'Ford']
number_of_cars_for_sale = [1000, 1200]
price_of_model = 37500.50
print ("The \"%s\" shop are expecting to sell %d units of the new %s model next year." % (car_shop[0], number_of_cars_for_sale[0], car_brand[0]), 
       "\t The \"%s\" shop are expecting to sell %d units of the new %s model next year." % (car_shop[1], number_of_cars_for_sale[1], car_brand[1]))

# replace + with \t