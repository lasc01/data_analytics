s = 'Administrative expenses'
s1 = s.replace("Administrative", "Selling")
# print(s1)
# print(s.startswith("Admin"))

# splitting operators
# print(s1.split())
# this also gives the same result
# print(s1.split(" "))
# splitting at "s"
# print(s1.split("s"))
# print(len(s1))

s2 = "personal ID, first name, last name, date of birth, place of birth, city of birth"
list_01 = s2.split(",", 6)
# print(list_01)

# lowercase. This changes all characters to lower case
s = 'Administrative expenses'
print(s.lower())
# This changes all characters to upper case
print(s.upper())
# this changes every first letter in a word to uppercase
print(s.title())

# this removes all the white space at the right hand side
name1 = 'Martin Peterson   '
# print(name1.rstrip())

import pandas as pd
name = pd.Series(["Martin Peterson", "John Fitzpatrick", "Kate Cruz"])
print(name)