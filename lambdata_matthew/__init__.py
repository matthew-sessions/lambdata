import pandas as pd
import numpy as np

ONES = pd.DataFrame(np.ones(30))

def add_col(df, li,name):
  df = df
  df[name] = li
  return(df)
