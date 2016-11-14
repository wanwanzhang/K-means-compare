
import random
import sys
import os
import pandas as pd
from pylab import *
from scipy.cluster.vq import *
from numpy import *
from PIL import *

# generate test data
# generate 100 rows and 2 columns

class1 = 1.5 * random.randn(100, 2)
print(class1)
class2 = random.randn(100, 2) + array([5, 5])
# print(class2)
features = vstack((class1, class2))
#print(features[0:1])
#print("wanttttt")

# K-Means clustering
centroids, variance = kmeans(features, 2)
# print(centroids)
#print("varancccc")
# print(variance)
code, distance = vq(features, centroids)
print(vq(features, centroids))
# print(distance)
figure()

ndx = where(code == 0)[0]
print(ndx)
plot1 = plot(features[ndx, 0], features[ndx, 1], '*')
#show(plot1)

ndx = where(code == 1)[0]
plot2 = plot(features[ndx, 0], features[ndx, 1], 'r.')
#show(plot2)

plot3 = plot(centroids[:,0],centroids[:,1],'go')
#show(plot3)

axis('off')
show()

