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

numTrials = 5
numFolds = 10 #numFolds-fold cross-validation
minK, maxK = 10, 20 #Only look in interesting range (inclusive)
kCostPairs = []
for clusters in xrange(minK, maxK+1): 
    minCost = None
    bestModel = None
    for trial in xrange(numTrials):
        model = KMeans.train(rdd3, clusters)
        cost = model.computeCost(rdd3)
        # We're not saving average cost, only minimum cost,
        # because many trials will produce suboptimal clusterings
        if minCost == None or cost < minCost:
            minCost = cost
            bestModel = model
    print clusters, minCost
    kCostPairs.append((clusters, minCost))

# save data
import csv
with open("kmeans-sans-crossval.csv", "wb") as csvfile:
    datawriter = csv.writer(csvfile)
    for pair in kCostPairs:
        datawriter.writerow(pair)
