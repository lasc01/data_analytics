# for i in range(2):
    # for j in range(5):
        # print(i, j, end=" ")

# Another example

products = ["Product A", "Product B"]
costs = [1000, 2000, 3000, 4000]
time_horizon = (1,3,12)

for i in products:
    for j in costs:
        for k in time_horizon:
            print("expected sales for {0} month(s) for {1} is: ${sales}".format(k, i, sales=j*k) )

# another exanple 
            products_on_sale = ['Chair_Type_1', 'Chair_Type_2', 'Chair_Type_3', 'Chair_Type_4']
sale_prices = [100, 120, 135, 150]
quantities = [1000, 1500, 1300]

for chair_type in products_on_sale:
    for price in sale_prices:
        for quantity in quantities:
            print("Expected revenue for {chair} if {quant} chairs are to be sold: {amt}".format(chair = chair_type, quant = quantity, amt = price * quantity))