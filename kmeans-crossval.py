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

def shallowCopy(A):
    return [A[i] for i in xrange(len(A))]

numTrials = 5
numFolds = 10 #numFolds-fold cross-validation
minK, maxK = 10, 20 #Only look in interesting range (inclusive)
kCostPairs = []
for clusters in xrange(minK, maxK+1): 
    minCost = None
    bestModel = None
    rddPartitions = rdd3.randomSplit([1]*numFolds)
    for fold in xrange(numFolds):
        rddPartitionsTemp = shallowCopy(rddPartitions)
        rdd_test = rddPartitionsTemp.pop(fold)
        rdd_train = sc.union(rddPartitionsTemp) #everything except fold
        for trial in xrange(numTrials):
            model = KMeans.train(rdd_train, clusters)
            cost = model.computeCost(rdd_test)
            # We're not saving average cost, only minimum cost,
            # because many trials will produce suboptimal clusterings
            if minCost == None or cost < minCost:
                minCost = cost
                bestModel = model
    print clusters, minCost
    kCostPairs.append((clusters, minCost))

# save data
import csv
with open("kmeans-crossval.csv", "wb") as csvfile:
    datawriter = csv.writer(csvfile)
    for pair in kCostPairs:
        datawriter.writerow(pair)

#[(10, 3179533338955.3486), (11, 2711544522925.3823), (12, 2220900749934.583), (13, 1672991507263.8196), (14, 1263718821074.5535), (15, 781428159622.5408), (16, 812027361935.4075), (17, 747212406263.9656), (18, 750801047612.2462), (19, 740621543755.676), (20, 709223156336.2871)]


