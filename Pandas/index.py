import pandas as pd

workers_age = {'Amy White':50, 'Jack Stewart':53, 'Richard Lauderdale':35, 'Sara Johnson':43}
workers_age = pd.Series(workers_age)

print(workers_age.index)

import pandas as pd
employees_work_exp = pd.Series({"Martin": 8, "George": 5})
print(employees_work_exp)