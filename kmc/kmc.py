import numpy as np
from time import time
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics
# See:
# https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html 
# https://scikit-learn.org/0.18/auto_examples/cluster/plot_kmeans_digits.html

digits = load_digits()
data = scale(digits.data)   # N digits

y = digits.target           # Labels

k = len(np.unique(y))

samples, features = data.shape

def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))
    
clf = KMeans(n_clusters=k, init="random", n_init=10)        # Classifier
bench_k_means(clf, "1", data)