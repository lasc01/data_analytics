import numpy as np

ran_test_data = np.genfromtxt("Lending-company.csv", delimiter=",")
# print(ran_test_data)

# print(np.isnan(ran_test_data[:,-2]).sum())
temp_nan = np.nanmax(ran_test_data[:,-2].round(2) + 1)
# print(temp_nan)

ran_test_data = np.genfromtxt("Lending-company.csv", delimiter=",", filling_values = temp_nan)
# print(ran_test_data[:,-2].round(2))

temp_mean = np.nanmean(ran_test_data[:,-2])
# print(temp_mean.round(2))

# print(np.nanmax(ran_test_data[:,-2]))
# print(np.nanmin(ran_test_data[:,-2]))

for i in ran_test_data[:,-2]:
    ran_test_data[:,-2] = np.where(ran_test_data[:,-2] == temp_nan,
                                  temp_mean,
                                  ran_test_data[:,-2])
    
print(ran_test_data[:,-2].round(2))