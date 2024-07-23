# lambda is used to create an anonymous function
print((lambda x: x**2)(3))

# Lambda can also use another annonymous function as a parameter
square_num = lambda x,y : x + y(x)

print(square_num(3, lambda x: x**2))

print((lambda x: x*10)(7))