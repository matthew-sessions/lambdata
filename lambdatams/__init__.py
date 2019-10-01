import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs

ONES = pd.DataFrame(np.ones(30))

def add_col(df, li,name):
  df = df
  df[name] = li
  return(df)

def wiki_content(url):
  #enter a wiki URL to see info about text.
  ge = requests.get(url)
  soup = bs(ge.content, 'html.parser')
  title = soup.find('h1').text
  para = soup.find_all('p')
  para_list = [i.text for i in para if i.text != '\n']
  para_len = len(para_list)
  word_count =  sum([len(i.split(' ')) for i in para_list])

  print(f"The wiki page about {title} has {para_len} paragraphs with a total of {word_count} words!")

  return(word_count)
