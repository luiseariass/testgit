import qgrid
import numpy as np
import pandas as pd
from ipywidgets import interact, interact_manual
import ipywidgets as widgets

df = pd.read_csv('../data/iris_dataset.csv')
df.head()

qgrid_view = qgrid.show_grid(df, show_toolbar=True)
qgrid_view