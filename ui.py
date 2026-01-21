import streamlit 
import os , pandas as pd
import sys , time
import plotly.express as fancyplot

import matplotlib.pyplot as plotlib
import matplotlib


data = pd.read_csv("dataset.csv")

print(data)

sets = data.groupby("Genre").all()

print(sets)

def find(name:str):
    tmplist = []
    for x in data["Title"]:
        if name in x:
            tmplist.append(x)

    return tmplist


votes = data["Votes"]

title = data["Title"]

graph = fancyplot.bar(y=votes,x=title)

streamlit.plotly_chart(graph)