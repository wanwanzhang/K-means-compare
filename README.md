# K-means-compare

Compare the old version with SKlearn k-means

This project applies the KMeans algorithm by importing SKlearn. 
Data has been clustered from iris, here have three results,of which two clusters were gotten by KMeans algorithm.
and one of them is maded to performence worse purposely by setting algorithm paramater.
To compare results, k_mean_iris_3 is closer with the truth one, only some points which are in boundary make mistakes. 
but the k_means_iris_bad_init, which we randomly choose the centroid and deside to cluster only once.
as we can see, the results not good, more mistakes around the boundary. 

Conclusion: 
The preprocess of the k-means clustering is very important, especially dealing with outlies and standard format data.
and for the k value, we can try to do loop more times under different k, but usually not too many clusters , otherwise it will lose the meanng of clustering.
every cluster should have the special value itself, could be able to explain something, it is easier to read and identify if the special value are more different.
