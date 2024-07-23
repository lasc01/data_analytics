import numpy as np

# this is for the loadtxt function

landing_comp_num_1 = np.loadtxt("importing_text_file/Lending-Company-Numeric-Data.csv", delimiter= ",")
# print(landing_comp_num_1)

# this is for the genfromtxt function

landing_comp_num_2 = np.genfromtxt("importing_text_file/Lending-Company-Numeric-Data.csv", delimiter= ",")
# print(landing_comp_num_2)

#Although the loadtxt function loads data faster, but it tends to break
# if there is a missing data from the data set. 
# therefore, it is adviseable to always use the genfromtxt function
# when obtaining data from an external source

landing_comp_num_NAN = np.genfromtxt("importing_text_file/Lending-Company-Numeric-Data-NAN.csv", 
                                     delimiter= ";",
                                     skip_header=2,
                                     skip_footer=2,
                                     usecols= (0,2,4),
                                     unpack= True)
# the skip_header & footer skips the first 2 and last 2 rows of the dataset
# the usecols parameter selects the colums you want displayed
# the unpack = true parameter enhables the column to be separated individually
# i.e you can give 3 variable name to each  and separating with a ,
# print(landing_comp_num_NAN)

# saving data with numpy using np.save(npy)

landing_comp = np.genfromtxt("importing_text_file/Lending-company.csv", 
                                     delimiter= ",",
                                     dtype= str)
# use np.save to the file as npy
df_lending_comp_save = np.save("lending-comp_np", landing_comp)
# use np.load to load the file
load_lending_comp = np.load("lending-comp_np.npy")
# to check whether the .csv and . npy file format are thesame
# print(np.array_equal(load_lending_comp, landing_comp))
# print(load_lending_comp)

# saving data with numpy using np.savez(.npz)

landing_comp_1 = np.genfromtxt("importing_text_file/Lending-company.csv", 
                                     delimiter= ",",
                                     dtype= str)
landing_comp_num = np.loadtxt("importing_text_file/Lending-Company-Numeric-Data.csv", 
                              delimiter= ",",
                              dtype = str)
# np.savez can save more than one array at a time 
df_lending_com_save = np.savez("new-lending-savez", landing_comp_1, landing_comp_num)

lending_com_load = np.load("new-lending-savez.npz")
# in order to display a result, you have to specify the array you want to load
# therefore, arr_0 displace array 1, arr_1 displace array 2 
print(lending_com_load["arr_1"])

# saving data into text file using np.savetxt()

landing_comp_1 = np.genfromtxt("importing_text_file/Lending-company.csv", 
                                     delimiter= ",",
                                     dtype= str)
lending_com_1_save = np.savetxt("Lending-company.txt", 
                                landing_comp_1,
                                fmt= "%s",
                                delimiter= ",")
lending_com_1_load = np.genfromtxt("Lending-company.txt",
                                    delimiter= ",",
                                    dtype= str)
print(lending_com_1_load)