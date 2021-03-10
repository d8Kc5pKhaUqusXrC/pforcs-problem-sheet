# plottask.py
#
# A program that that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3
# in the range [0, 4] on the one set of axes.
#
# author: Mark Brislane
# date: 2021/03/10

import numpy as np
import matplotlib.pyplot as plt

# Generate the X Axis - 0 -> 4
# Graph looks a lot prettier if you change the range to include negative -> positive, i.e. -5 -> +4
xpoints = np.array(range(0, 4))

# Generate the 3 Y Axes - x, x^2 and x^3
f_ypoints = xpoints  # x
g_ypoints = xpoints * xpoints  # x squared
h_ypoints = xpoints * xpoints * xpoints  # x cubed

# Plot each graph, with pretty colours and labels
plt.plot(xpoints, f_ypoints, color="r", label="x")
plt.plot(xpoints, g_ypoints, color="g", label="x squared")
plt.plot(xpoints, h_ypoints, color="b", label="x cubed")

# Apply some labels to make the graph extra pretty and hopefully get some extra marks :-)
plt.title("f(x)=x, g(x)=x2 and h(x)=x3")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show this legend of a graph!
plt.legend()
plt.show()