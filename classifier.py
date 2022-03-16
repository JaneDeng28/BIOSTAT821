'''
# Implementing a classifier

Choose one of these two simple classifiers:

* [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
* [Fisher's linear discriminant](https://en.wikipedia.org/wiki/Linear_discriminant_analysis#Fisher's_linear_discriminant)

Implement it from scratch in Python. Here "from scratch" means that you may use standard modules (that come with Python) and `numpy`, and nothing else.

Make a visualization using `matplotlib` showing the decision surface for your classifier with some test data. 

## Submission

* You may work in groups of up to 3.
* Submit on Sakai:
  1. your implementation code as one or more `.py` files
  2. an image (jpeg/png) of your classifier visualization

'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sqlalchemy import false

def KNeighborsClassifier(X, Y, K = 6):
    if len(X) >= K:
        print("Choose a larger K")
    
    dist = []
    for x in X:
        for features in x[X]:
            euclidean_dist = np.sqrt(np.sum(np.array(features) - np.array(Y))**2)
            dist.append([euclidean_dist, x])
        sorted_dist = sorted(dist)
        for i in sorted_dist:
            kind = i[1]
        nearest = kind[:K]
        freqs = [(topkind, np.count_nonzero(topkind)) for topkind in nearest]
        x_res = (np.amax(freqs))[0]
        confi = (np.amax(freqs))[1] * 1.0 / K
    return x_res, confi, sorted_dist[K-1][0]

if __name__ == '__main__': 
    data = {'yes': [[1, 3], [1, 2], [2,3]], 'no':[[6, 6], [7, 9], [8, 6]]}
    Y = [[3.3, 6.5]]
    plot1 = plt.figure()
    ax = plot1.add_subplot(222)

    K = 3
    for i in data:
        for j in data[i]:
            pyplot.scatter(i[0], j[1], s = 50, color = 'blue')
    x, confi, radius_val = KNeighborsClassifier(data, Y, K)
    print(x, confi, radius_val)
    pyplot.scatter(Y[0], Y[1], s = 100, color = 'red')
    circle = pyplot.Circle(xy = Y, radius = radius_val, color = 'green', fill = False)
    ax.add_patch(circle)
    pyplot.show()