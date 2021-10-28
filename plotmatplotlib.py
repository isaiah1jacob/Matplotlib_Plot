# import library

import matplotlib.pyplot as plt

# Define axes

left = 0.01
width = 0.9
bottom  = 0.01
height = 0.9
right = left + width
top = bottom + height
ax = plt.gca()

# Transform axes

ax.set_transform(ax.transAxes)

# Define text

ax.text(left, top, 'left top',
        horizontalalignment='left',
        verticalalignment='top',color='r',size=10,
        transform=ax.transAxes)

# Display Graph

plt.show(