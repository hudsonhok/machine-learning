# K-Means Algorithm

## What is it?
K-means clustering is an algorithm that serves to split a dataset into “clusters” of points that share similarities.
1. The first step is to choose the number of clusters, k.
2. Select and initialize k random points as centroids. These points serve as the center of the k clusters.
3. Assign the points to the closest centroid. This involves calculating the Euclidean distance from each of the centroids then assigning the
point to the one with the smallest distance.
4. Calculate the average of the data points in each cluster, and use each average as the new centroid of the cluster
5. Repeat steps 3 and 4 until the centroids no longer change.
6. Once there are no more changes in the centroids, you can again assign each point to the closest cluster by calculating the Euclidean distance to each cluster.
7. The final step is to analyze the results for significant findings.