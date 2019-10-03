import requests


class Weather:
    def __init__(self, key, lat, lon):
        """Pass in the Darksky API and the lat and lon of any given location"""
        a = requests.get('https://api.darksky.net/forecast/'+ key + '/' + str(lat)+ ',' + str(lon) +'?extend=hourly')
        if a.ok == True:
            self.response = a
            self.dic = a.json()
        else:
            print('Make sure you lat, lon, or API key is correct.')

    def getdf(self):
        """return the hourly data as a dataframe"""
        if self.response.ok == True:
            dic = self.dic['hourly']['data']
            df = pd.DataFrame(dic)
            return(df)
        else:
            print('make sure your api data is correct')
