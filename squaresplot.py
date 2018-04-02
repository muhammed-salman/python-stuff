import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

#sec 3
input_values = [1, 2, 3, 4, 5]
#end sec 3

squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)
#end of sec3
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)

plt.xlabel("Value", fontsize=14)

plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
#end of sec 2

plt.show()
