import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def scatter_plot(df, x, y, z):
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	inliers = df[df['outlier'] == False]
	outliers = df[df['outlier'] == True]

	ax.scatter(inliers[x], inliers[y], inliers[z], marker='o',
		label="inliers", c="green")

	ax.scatter(outliers[x], outliers[y], outliers[z], marker='x',
		label="outliers", c="red")

	ax.set_xlabel(x)
	ax.set_ylabel(y)
	ax.set_zlabel(z)
	ax.set_title('sampled inliers and outliers')
	ax.legend()
	
	plt.show()