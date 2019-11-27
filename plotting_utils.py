import matplotlib.pyplot as plt

def scatter_plot(x, y, x_label, y_label="rental price"):
	plt.scatter(x, y)
	plt.ylabel(y_label)
	plt.xlabel(x_label)
	plt.show()