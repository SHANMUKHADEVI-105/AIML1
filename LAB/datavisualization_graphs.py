# -*- coding: utf-8 -*-
"""DataVisualization-GRAPHS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PgBGmhxSyGgVdJr35Zqinat7xS8oMggN
"""

from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show

from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='k')
plt.show()

from matplotlib import pyplot as plt
plt.bar([0.25,1.25,2.25,3.35,4.25],[50,40,70,80,20], label="BMW",color='g',width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60], label="Audi",color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()

import matplotlib.pyplot as plt
population_age = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age,bins,histtype='bar',rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Interesting Graph')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a 3x3 grid of subplots
fig, axs = plt.subplots(3, 3, figsize=(10, 10))
central_ax = axs[1, 1]
central_ax.plot(x, y)
central_ax.set_title('Central Plot')
for i in range(3):
    for j in range(3):
        if i != 1 or j != 1:
            axs[i, j].axis('off')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot with a digital style
plt.figure(figsize=(10, 6))

# Plot data
plt.plot(x, y, color='cyan', linestyle='-', linewidth=2, marker='o', markersize=6)

# Set title and labels with a digital theme
plt.title('Digital Style Plot', fontsize=16, fontweight='bold', color='white', backgroundcolor='black')
plt.xlabel('X-axis', fontsize=14, color='white')
plt.ylabel('Y-axis', fontsize=14, color='white')

# Customize grid and axes
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.gca().set_facecolor('black')  # Set background color of the plot area
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['left'].set_color('white')
plt.gca().spines['bottom'].set_color('white')
plt.gca().tick_params(axis='both', colors='white')

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Data to plot
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode the 1st slice

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)

# Set the aspect ratio to be equal, so that pie is drawn as a circle
plt.axis('equal')

# Set the title
plt.title('Pie Chart Example')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create an area plot
plt.figure(figsize=(10, 6))

# Plot the first area
plt.fill_between(x, y1, color='skyblue', alpha=0.4, label='sin(x)')

# Plot the second area
plt.fill_between(x, y2, color='lightcoral', alpha=0.6, label='cos(x)')

# Add labels, title, and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot Example')
plt.legend(loc='upper right')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot on the first subplot
axs[0, 0].plot(x, y1, 'r-')
axs[0, 0].set_title('Sine Wave')

# Plot on the second subplot
axs[0, 1].plot(x, y2, 'g--')
axs[0, 1].set_title('Cosine Wave')

# Plot on the third subplot
axs[1, 0].plot(x, y3, 'b-.')
axs[1, 0].set_title('Tangent Wave')
axs[1, 0].set_ylim([-10, 10])  # Limit y-axis values for better view

# Plot on the fourth subplot
axs[1, 1].plot(x, y4, 'm:')
axs[1, 1].set_title('Exponential Function')

# Add labels and title
for ax in axs.flat:
    ax.set(xlabel='X-axis', ylabel='Y-axis')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'])

# Add labels and title
plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Box Plot Example')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate example data
np.random.seed(0)
data = np.random.rand(10, 10)  # 10x10 matrix of random numbers

# Create a heatmap
plt.figure(figsize=(8, 6))
ax = sns.heatmap(data,
                 cmap='YlGnBu',  # Color map
                 annot=True,     # Annotate cells with data values
                 fmt=".2f",      # Format of the annotation
                 center=0.5,     # Central value for color scaling
                 linewidths=0.5, # Width of lines separating cells
                 cbar_kws={"shrink": .8}  # Colorbar scaling
                )

# Add title
plt.title('Central Heatmap Example')

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a simple line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')  # Line with markers
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.grid(True)  # Add grid lines for better readability

# Show the plot
plt.show()