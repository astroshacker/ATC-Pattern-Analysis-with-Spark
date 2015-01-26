#Program 1: Print the first ten lines of the dataset.
    >>> line = sc.textFile("hdfs://<master-DNS>:9000/rita")
    >>> line.take(10)
    
#Program 2: Count how many times the string "SJC" appears.
    >>> wiki = sc.textFile("hdfs://<master-DNS>:9000/rita")
    >>> berkeley_pages = wiki.filter(lambda x: "SJC" in x)
    >>> berkeley_pages.count()
    OR
    >>> wiki = sc.textFile("hdfs://<master-DNS>:9000/rita")
    >>> b = wiki.filter(lambda line: "SJC" in line)
    >>> b.count()

#Program 3: Count (?)
    >>> sc.parallelize([1, "ABC", (1, 2)]).count()

#Program 5: Count # of times "SJC" appears. Standalone!
	import sys
	from pyspark import SparkContext
	logFile = "hdfs://<master-DNS>:9000/rita"
	sc = SparkContext("local", "simple app")
	logData = sc.textFile(logFile).cache()
	numSJC = logData.filter(lambda line: 'SJC' in line).count()
	print "Lines with SJC: %i" % (numSJC)

#Program 6: Collect data from another column in a pipe-delimited text file (ex. file below code).
	>>> log = sc.textFile('hdfs://<master-dns>:9000/text/pipe-delimited.txt')
	>>> log = log.map(lambda line: line.split('|'))
	>>> log = log.filter(lambda x: x[2] == 'SJC')
	>>> log = log.map(lambda x: x[1])
	>>> log.collect()

"""
Year|Delay|Dest|Flight #
1987|-5|SJC|500
1987|-5|SJC|250
1987|07|SFO|700
1987|09|SJC|350
1987|-5|SJC|650
"""