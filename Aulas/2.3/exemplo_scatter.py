import matplotlib.pyplot as plt 
import numpy as np

x = [1,2,3,4,5,6,7,8,9]
y = [5,4,2,9,3,2,8,1,5]

plt.scatter(x,y, label = "pontos " , color = "b", marker = "*", s = 100)

plt.legend()

plt.show()
