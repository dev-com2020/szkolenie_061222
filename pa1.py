import pandas as pd
from pandasgui import show
from pandasgui.datasets import titanic
# gui = show(titanic)

zbior = pd.read_csv('worldcities.csv')
gui = show(zbior)