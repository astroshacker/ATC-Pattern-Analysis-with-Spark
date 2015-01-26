ATC Analysis with Apache Spark
This project uses Apache Spark to analyze a government database from Air Traffic Control data streams. The master branch contains Spark programs which run directly from the local shell, an external file, and the Pyspark shell. All databases are stored in an Amazon S3 bucket and the MapReduce function is carried out by 1 Master and 10 Slave Micro Instances in Amazon EC2.

The .csv database is also in the master.
