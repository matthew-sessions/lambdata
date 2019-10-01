import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs

ONES = pd.DataFrame(np.ones(30))

def add_col(df, li,name):
    df = df
    df[name] = li
    return(df)

class wiki:
    def __init__(self,url):
        #enter a wiki URL to see info about text.
        ge = requests.get(url)
        soup = bs(ge.content, 'html.parser')
        self.title = soup.find('h1').text
        para = soup.find_all('p')
        self.para_list = [i.text for i in para if i.text != '\n']
        self.para_len = len(self.para_list)
        self.word_count =  sum([len(i.split(' ')) for i in self.para_list])
        self.overview = f'The wiki page titled "{self.title}" has {self.para_len} paragraphs and a total of {self.word_count} words.'

    def title(self):
        #Return the wiki title
        return(self.title)

    def para_list(self):
        #Return a list of all the paragraphs
        return(self.para_list)

    def para_len(self):
        #Number of paragraps
        return(self.para_len)

    def word_count(self):
        #total word count in paragraphs
        return(self.word_count)

    def overview(self):
        print(self.overview)
