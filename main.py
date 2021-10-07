import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
avg = df["Avg Rating"].to_list()

fig = ff.create_distplot([avg],["Average"])
fig.show()