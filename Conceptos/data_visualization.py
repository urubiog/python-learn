# The time has arrived to harness the power of data visualization with matplotlib,
# where we transform raw data into insightful and aesthetically pleasing graphics.
# Whether it's simple line charts or complex multi-variable plots, matplotlib provides
# the tools to communicate the story behind the numbers.

print("Time for Data Visualization with Matplotlib!")

# Importing matplotlib for plotting
import matplotlib.pyplot as plt
import math
import random

# Basic Line Plot:
# A line plot is one of the simplest and most common ways to visualize continuous data.

# Create some data
x = [i * 0.1 for i in range(101)]  # 100 points between 0 and 10
y = [math.sin(i) for i in x]  # Sine function of x

# Basic line plot
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Scatter Plot:
# A scatter plot is used to display values for two variables, represented by points on the plane.

# Create random data
x = [i for i in range(50)]
y = [i**2 for i in x]  # Square of i

# Scatter plot
plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar Plot:
# A bar plot is useful for displaying categorical data or comparing quantities.

categories = ["A", "B", "C", "D"]
values = [23, 17, 35, 12]

# Bar plot
plt.bar(categories, values, color="green")
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Histogram:
# A histogram is used to represent the distribution of numerical data.

# Create random data for the histogram
data = [
    random.randint(1, 100) for _ in range(1000)
]  # 1000 random integers between 1 and 100

# Histogram plot
plt.hist(data, bins=30, color="blue", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Pie Chart:
# A pie chart is used to represent proportions of a whole.

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 30, 20, 10]

# Pie chart
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.show()

# Subplots:
# You can create multiple plots in the same figure using subplots.

# Generate subplots
fig, axs = plt.subplots(2, 2)  # 2x2 grid of plots
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Line Plot")
axs[0, 1].scatter(x, y, color="purple")
axs[0, 1].set_title("Scatter Plot")
axs[1, 0].bar(categories, values, color="orange")
axs[1, 0].set_title("Bar Plot")
axs[1, 1].hist(data, bins=30, color="brown", edgecolor="black")
axs[1, 1].set_title("Histogram")
fig.tight_layout()  # Adjust spacing
plt.show()

# Customizing the Plot:
# We can also customize the appearance of our plots, such as changing the colors, line styles, etc.

# Customization example
plt.plot(x, y, color="red", linestyle="--", linewidth=2)
plt.title("Customized Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Exercise:
# Create a plot that shows the trend of two variables over time. The first variable should represent
# a sine wave, and the second variable should represent a cosine wave.
# Both should be plotted on the same graph with different colors and labels.
