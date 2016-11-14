# K-means-compare

Compare the old version with SKlearn K-means

This project applies the KMeans algorithm by importing SKlearn. 
Data has been clustered from iris. Three results have been gotten here, of which two clusters were gotten by KMeans algorithm, one of them is made to perform worse purposely by setting algorithm parameter.
To compare results, k_mean_iris_3 is closer to the truth one. Only a few of points which are in boundary show mistakes. 
For the k_means_iris_bad_init, we randomly choose the centroid and decide to cluster only once.
As we can see, the result is not good, more mistakes show up around the boundary. 

Conclusion: 
The preprocess of the k-means clustering is very important, especially in case of dealing with outlies and standard format data.
For the k value, we can try to do loop more times under different k, but not too many clusters. Otherwise it will lose the meanng of clustering.
Every cluster should have the special value itself. It is easier to read and to identify if the special value are different.
