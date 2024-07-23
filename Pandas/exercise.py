import pandas as pd
import numpy as np
employee_names = pd.Series(["Amy White", "Jack Stewart", "Richard Lauderdale", "Sara Johnson"])
print(employee_names)

work_experience_years = pd.Series([5,8,3,10])
work_experience_years.name = "Work Experience (Yrs.)"

print(work_experience_years)

