import pandas as pd

employees_work_exp = pd.Series({
'Amy White'   : 3,
'Jack Stewart'   : 5,
'Richard Lauderdale'  : 4.5,
'Sara Johnson'  : 22,
'Patrick Adams' : 28,
'Jessica Baker'  : 14,
'Peter Hunt'   : 4,
'Daniel Lloyd'  : 6,
'John Owen'   : 1.5,
'Jennifer Phillips'  : 10,
'Courtney Rogers'   : 4.5,
'Anne Robinson'  : 2,
})

# note that this is non-numeric method(.head() & .tail())
print(employees_work_exp.tail())

# apply parameter and argument to specify the number of row you want to display
print(employees_work_exp.head(n=3))
# note tha n is the parameter while 3 is the argument to display the first 3 row
