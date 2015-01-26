#ATC Analysis with Apache Spark
This project uses Apache Spark to analyze a government database from Air Traffic Control data streams. The master branch contains Spark programs which run directly from the local shell, an external file, and the Pyspark shell. All databases are stored in an Amazon S3 bucket and the MapReduce function is carried out by 1 Master and 10 Slave Micro Instances in Amazon EC2. The .csv database is in the master branch for your convenience. With more data comes more patterns, and with more patterns comes improved predictability and efficiency.

By the end of this project, I hope to complete the following patterns:

1. Query, 3 trials, Tabulate Negative Delays, display MapReduce computing time, Array / Sum (int)
2. Query, 3 trials, Tabulate Positive Delays, display MapReduce computing time, Array / Sum (int)
3. Query, 3 trials, Display airport-centric delays in a list, display MapReduce computing time, Tuples (int)
4. Query, 3 trials, Average airport delays for each airport into one integer, display MapReduce computing time, Integer
5. Query, 3 trials, Display name of airport with worst weather forecast, display MapReduce computing time, String
