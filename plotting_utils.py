import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def scatter_plot(df, x, y, z):
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	sampled_df = df.sample(n=100)

	ax.scatter(sampled_df[x], sampled_df[y], sampled_df[z], marker='o')

	ax.set_xlabel(x)
	ax.set_ylabel(y)
	ax.set_zlabel(z)
	ax.set_title('scatter plot of sampled data')
	plt.show()