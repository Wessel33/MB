import requests
import pandas as pd

url = 'https://www.bonusbagging.co.uk/oddsmatching.php'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print (df)
df.to_csv('my data.csv')
