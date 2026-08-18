import matplotlib.pyplot as plt

# plt.plot([1,2,3],[4,52,6])

# plt.show()

x = ["maça","banana","kiwi", "pera"]
y = [2,4,6,1]

plt.bar(x,y, color = "green")

plt.xlabel("frutas")
plt.ylabel("quantidade")
plt.title("quantidade de frutas")

plt.show()

