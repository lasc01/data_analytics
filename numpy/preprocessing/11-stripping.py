import numpy as np

# Stippis the act of removing specific data from a string

lending_com_total_price = np.genfromtxt('numpy/Lending-Company-Total-Price.csv',
                                     delimiter = ',',
                                     dtype = np.str_,
                                     skip_header = 1,
                                     usecols = [1,2,4])

print(lending_com_total_price)

# To strip from the first, second and third colums

lending_com_total_price[:,0] = np.chararray.strip(lending_com_total_price[:,0], "id_")
lending_com_total_price[:,1] = np.chararray.strip(lending_com_total_price[:,1], "Product ")
lending_com_total_price[:,2] = np.chararray.strip(lending_com_total_price[:,2], "Location ")

print(lending_com_total_price)

# we can also use the np.where to transform letters in column 2 to numbers

# didn't work

# for i in lending_com_total_price[:,1]:
#     lending_com_total_price[:,1] = np.where(lending_com_total_price[:,1] == i,
#                                             add + 1,
#                                             lending_com_total_price[:,1]
#                                             )
    
lending_com_total_price[:,1] = np.where(lending_com_total_price[:,1] == 'A', 1,lending_com_total_price[:,1] )
lending_com_total_price[:,1] = np.where(lending_com_total_price[:,1] == 'B', 2,lending_com_total_price[:,1] )
lending_com_total_price[:,1] = np.where(lending_com_total_price[:,1] == 'C', 3,lending_com_total_price[:,1] )
lending_com_total_price[:,1] = np.where(lending_com_total_price[:,1] == 'D', 4,lending_com_total_price[:,1] )
lending_com_total_price[:,1] = np.where(lending_com_total_price[:,1] == 'E', 5,lending_com_total_price[:,1] )
lending_com_total_price[:,1] = np.where(lending_com_total_price[:,1] == 'F', 6,lending_com_total_price[:,1] )

print(lending_com_total_price)

#  We can use the astype() function to change this to an integer
print(lending_com_total_price.astype(dtype = np.float64).astype(dtype = np.int64))