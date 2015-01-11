import sys
from pyspark import SparkContext
    
logFile = "hdfs://<host-ip-address>:9000/<dataset folder>"
sc = SparkContext("local", "simple app")
logData = sc.textFile(logFile).cache()

numSJC = logData.filter(lambda line: 'SJC' in line).count()

print "Lines with SJC: %i" % (numSJC)
