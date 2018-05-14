#Extracts to .csv an html table

import requests
import pandas as pd

url = 'https://www.bonusbagging.co.uk/oddsmatching.php'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print (df)
df.to_csv('my data.csv')


# to take data: 
df.get_value(5,3,takeable=True) # (row index, col index, default=False (want true) )
