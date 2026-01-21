import sqlite3 as lite3
import pandas as pd


file = pd.read_csv(r"C:\Users\digital.library.MITWPU\Documents\project\dataset.csv")

connection = lite3.connect("data.sqlite3")

file.to_sql("Movies",connection,if_exists="replace")