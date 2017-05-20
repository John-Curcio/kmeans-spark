# Implementation of K-Means++ Algorithm in Spark context.

import math
import random
# I ran this code on the Pittsburgh Supercomputin Center's clusters,
# so ordinarily there'd be an "import pyspark" here.

# read in data from spark context
rdd1 = sc.textFile("5000_points.txt")
# massage the data into an RDD of x-y coordinate tuples
rdd2 = rdd1.map(lambda x: x.split())
rdd = rdd2.map(lambda x: (int(x[0]), int(x[1])) ) #final RDD to be used.

# kmeans++ uses a clever initialization scheme to set the cluster centers

def eucDist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

# Given a data point x, and a list of cluster centers, 
# findNearestCenterAndDist returns the nearest center to x, and its distance 
# from x, in that order.
def findNearestCenterAndDist(x, centers):
    minEucDist = None
    nearestCenter = None
    for center in centers:
        if center != None:
            dist = eucDist(center, x)
            if minEucDist == None or dist < minEucDist:
                nearestCenter = center
                minEucDist = dist
    # minEucDist != None iff there exists >= 1 non-None element in centers
    return nearestCenter, minEucDist

def kMeansPlusPlus(numClusters):
    centers = [None]*numClusters
    centers[0] = rdd.takeSample(False, 1)
    # initialization step
    for i in range(1, numClusters):
        rddCenterScores = rdd.map(lambda x: findNearestCenterAndDist(x, centers)[1]**2)
        scoreSum = rddCenterScores.reduce(lambda x, y: x+y)
        rddCenterProbs = rddCenterScores.map(lambda x: x // scoreSum)
        # TODO: select datapoints in rdd to be initial cluster centers,
        # each with probability in the corresponding index of rddCenterProbs
        


