numbers = [2,4,5,6,7]
new_numbers = []
for n in numbers:
    new_numbers.append(n*2)
# print(new_numbers)

# Ashorter way of getting same output is 
mult_2 = [n * 2 for n in numbers]
# print(mult_2)

# Amore complex example involving conditional
cubic_num = [num ** 3 for num in range(1,10) if num%2 != 0]
# print(cubic_num)

# print([num*10 for num in range(1, 11) if num % 2 == 0])
multiples_of_10 = []
for num in range(1,11):
    if num % 2 == 0:
        multiples_of_10.append(num*10)
print(multiples_of_10)