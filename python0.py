# -*- coding: utf-8 -*-
"""
Write a list comprehension which will build a list of items: [‘Mike 1’, ‘Mike 2’, …, ‘Mike 100’]. The list should have 100 items.
"""

["Mike {}".format(i) for i in range(1, 101)]

"""Write a Python code which will merge all item from the dictionaries: dict1 and dict2. Assume, that values from dict1 are more important. So if the there are two items with the same key in both dictionaries but with different values the value from dict1 should remain in the result.

So, for the values:
d1 = { ‘a’: 12, ‘b’: 45}
d2 = { ‘a’: 66, ‘c’: 88}

The expect result is:
{‘a’: 12, ‘b’: 45, ‘c’: 88}
"""

dict(list(d2.items()) + list(d1.items()))

"""Write a Python code declaring and solving the following system of equations with Numpy. Use Numpy linalg.solve(a, b) function to find solution.

5x + 6y - z = 4
-2x -y + 5z = -1
-3x +y + 4z = 2
"""

import numpy as np

A = np.array([[5, 6, -1], [-2, -1, 5], [-3, 1, 4]])
B = np.array([4, -1, 2])
X = np.linalg.solve(A,B)

print(X)

"""Write a Python code which will initialize a Pandas DataFrame with 7 columns and 10 rows of random numbers. The labels for the columns should be A,B,C,D,E,F,G and the random numbers should be with the range: 10-20."""

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(10,20, size=(10,7)))
df.rename(columns={0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G"})

"""Assign a label to each backend related to iteractivity: (interactive, -non-interactive):

a) Qt4
b) Agg
c) Png
d) Pdf
e) Plotly
f) Bokeh
"""

#a) Qt4 - interactive
#b) Agg - mostly non-interactive
#c) Png - non-interactive
#d) Pdf - non-interactive
#e) Plotly - interactive
#f) Bokeh - interactive

"""Python code (full with imports) which will plot using matplotlib the following plot with the annotation:

Hint for the annotate function:

plt.annotate('????', (xp, yp), xytext=(???, ???), arrowprops={'arrowstyle':'->'} )
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x) + 5)
plt.plot(x, np.cos(x) + 4)
plt.annotate('intersection p=(4.7, 4)', xy=(4.7, 4), xycoords='data',
             xytext=(4.7, 3.5), textcoords='data',
             arrowprops=dict(facecolor='black', width=1))
