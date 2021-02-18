""" 
quick way to find the international space station and plot it to a map

"""

import pandas as pd 
import plotly.express as px

#api call to grab the lat/lon coords of the iss
url = 'http://api.open-notify.org/iss-now.json'

#build a dataframe to contain the info
df = pd.read_json(url)
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)
df = df.drop(['index','message'], axis=1)

#plot the iss coords onto a map using plotly
fig = px.scatter_geo(df, lat='latitude', lon='longitude')
fig.show()