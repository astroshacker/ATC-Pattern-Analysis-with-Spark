#Counts the number of arrivals to/departures from SJC.

import sys
from pyspark import SparkContext
    
logFile = "hdfs://ec2-<ec2-IP>:9000/<folder where dataset is located>"
sc = SparkContext("local", "simple app")
logData = sc.textFile(logFile).cache()

numSJC = logData.filter(lambda line: 'SJC' in line).count()

print "Lines with SJC: %i" % (numSJC)
