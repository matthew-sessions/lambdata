import pandas as pd

def grab(df):
  #insert you dataframe do see all the NaN values.
  return(pd.DataFrame(df.isna().sum().sort_values(ascending=False), columns=['NaN Total']))
