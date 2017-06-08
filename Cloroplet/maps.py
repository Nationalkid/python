import plotly
import plotly.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
df
df1 = pd.read_csv('C:/Users/Elena Arsevska/Dropbox/Savsnet_main_work/Notebooks/Cloroplet/map.csv',encoding = "ISO-8859-1")
df1
py.sign_in('PauloPimenta', 'dehPQ8xFFpN0VrkIVT9i')

data = [ dict(
        type = 'choropleth',
        locations = df1['code'],
        z = df1['total'],
        text = df1['name'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            #autotick = False,
            #tickprefix = 'Total',
            title = 'Frequency of travelings'),
      ) ]

layout = dict(
    title = 'Dummy data pet travelings around the word',# <br>Source:\
            #<a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            #CIA World Factbook</a>',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
#py.plot( fig, validate=False, filename='pet_travel_map' )
plotly.offline.plot(fig,filename='test')

