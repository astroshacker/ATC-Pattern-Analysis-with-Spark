#Counts the number of arrivals to/departures from SJC.

import sys
from pyspark import SparkContext
    
logFile = "hdfs://ec2-54-173-109-80.compute-1.amazonaws.com:9000/rita"
sc = SparkContext("local", "simple app")
logData = sc.textFile(logFile).cache()

numSJC = logData.filter(lambda line: 'SJC' in line).count()

print "Lines with SJC: %i" % (numSJC)
