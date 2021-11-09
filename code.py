import csv
import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("data.csv")

graph = ff.create_distplot([data["Height(Inches)"].tolist()],["Height"],show_hist= False)

graph.show()