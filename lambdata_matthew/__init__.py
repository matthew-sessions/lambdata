import pandas as pd
import numpy as np

ONES = pd.DataFrame(np.ones(30))


def add_col(df, li,name):
  #add new column to data frame. 
  #Insert a dataframe, list and name of the new column  
  df = df
  df[name] = li
  return(df)
