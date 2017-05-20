# This is an extension of code from a workshop hosted by the Pittsburgh 
# Supercomputing Center, which I attended. I 

# I ran this code on the Pittsburgh Supercomputing Center's clusters,
# so ordinarily there'd be an "import pyspark" here.

# read in data from spark context
rdd1 = sc.textFile("5000_points.txt")
# massage the data into an RDD of x-y coordinate tuples
rdd2 = rdd1.map(lambda x:x.split())
rdd3 = rdd2.map(lambda x: [int(x[0]),int(x[1])])

rdd3.persist(StorageLevel.MEMORY_ONLY)

from pyspark.mllib.clustering import KMeans

for clusters in range(1,30):
    model = KMeans.train(rdd3, clusters)
    print clusters, model.computeCost(rdd3)

for trials in range(10): #Try ten times to find best result
    for clusters in range(12, 16): #Only look in interesting range
        model = KMeans.train(rdd3, clusters)
        cost = model.computeCost(rdd3)
        centers = model.clusterCenters #Let’s grab cluster centers
        if cost<1e+13: #If result is good, print it out
            print clusters, cost
        for coords in centers:
            print int(coords[0]), int(coords[1])

#TODO: actual cross-validation





