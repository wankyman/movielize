import streamlit 
import os , pandas as pd
import sys , time , aiohttp
import plotly.express

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


# name = input("Enter Movie to find: ")

# result = find(name)

# print(result)
