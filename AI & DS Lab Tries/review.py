"""
Matrix operations, Programs using matplotlib / plotly /
bokeh / seaborn for data visualisation and programs to handle data using pandas
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import bokeh.plotting as bp
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models.widgets import Panel, Tabs
from bokeh.layouts import column
from bokeh.io import output_file, show

# =============================================================================
# Matrix operations
# =============================================================================

# Matrix addition

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

C = A + B
print(C)

# Matrix subtraction

C = A - B
print(C)

# Matrix multiplication

C = A * B
print(C)

# Matrix division

C = A / B
print(C)

# Matrix transpose

C = A.T
print(C)

# Matrix inverse

C = np.linalg.inv(