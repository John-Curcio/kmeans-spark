# Disclaimer

This is an extension of code from a workshop hosted by the Pittsburgh Supercomputing Center, which I attended. This is mostly to familiarize myself with Spark, and also to show off my understanding of some fundamental machine learning concepts.

I ran this code on the Pittsburgh Supercomputing Center's clusters, so the importing of modules might look a little funny in this code. I consider it a fairly innocuous difference that might have to be corrected by the user anyway.

# So what are we looking at? 

`kmeans-crossval.py` uses cross-validation to find the optimal number of cluster centers. The k-means algorithm requires that `k` be specified initially.

Furthermore, aside from the cross-validation approach that I use here, I know of no general way to check that the number of clusters is indeed optimal. In my machine learning class, it was suggested that we look for "elbow points" in the curve of cost as a function of `k`, i.e. by eyeballing a graph. Note that this (master's level) class was hosted by CMU, which has the largest machine learning department in the world, as well as the best [data science club](cmudsc.org) in the world. *Clearly*, cross-validation is an improvement.

`kmeanspp.py` is an implementation of the k-means++ algorithm, which improves Lloyd's algorithm by cleverly initializing cluster centers. I'm pretty sure Spark's MlLib's KMeans is already an implementation of this. It's probably faster, too! But this wasn't tough for me to implement myself, and it shows that my machine learning fundamentals are half-decent at worst.
