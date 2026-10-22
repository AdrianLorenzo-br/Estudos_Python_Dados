import numpy as np 
import matplotlib.pyplot as plt

funcionarios = np.array(["adrian", "luiz", "carlos","alfonso"])
salarios = np.array([1900,2000,1200,5053])

plt.bar(funcionarios, salarios)

plt.xlabel("funcionarios")
plt.ylabel("salarios")
plt.title("salarios de funcionarios")

plt.show()




