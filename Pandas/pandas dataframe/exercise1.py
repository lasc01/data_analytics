# This is how we create a data frame from a numpy array from scratch

import pandas as pd
import numpy as np

array_a = np.array([[3,1,2], [6,3,2]])

df = pd.DataFrame(array_a, 
                  columns = ['col 1', 'col 2', 'col 3'],
                  index = ['row 1', 'row 2']
                  )

print(type(df))
print(df)