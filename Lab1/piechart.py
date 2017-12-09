from matplotlib import pyplot

labels = ['Mac', 'PC', 'LINUX']
colors = ['#a51855 ', '#7d41a3', 'yellow']
data = [2, 20,1]

pyplot.pie(data, labels =labels, colors =colors)
pyplot.axis('equal')
pyplot.show()
