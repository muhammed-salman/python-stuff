# import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)


plt.scatter(3, 5)
plt.scatter(4, 20, s=200)
plt.scatter(5, 8)
#sec 2
plt.scatter(2, 10, s=200)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both',which='major',labelsize=14)
#end sec 2
plt.show()
