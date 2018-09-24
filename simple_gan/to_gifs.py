from PIL import Image 
import numpy as np

path = "plots/features/feature_transform_%d.png"
import imageio 
images = []
for i in range(11):
	images.append(imageio.imread(path%(i*1000)))
imageio.mimsave('images/feature_transform.gif', images, fps=2)

path2 ="plots/features/feature_transform_centroid_%d.png"
images = []

for i in range(11):
	images.append(imageio.imread(path2%(i*1000)))
imageio.mimsave('images/feature_transform_centroid.gif', images, fps=2)

ipath = "plots/iterations/iteration_%d.png"
images = []
for i in range(11):
    images.append(imageio.imread(ipath%(i*1000)))
imageio.mimsave('images/iterations.gif', images, fps=2)

