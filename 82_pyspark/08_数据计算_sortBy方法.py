from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "E:/Python/python3.11.7/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# reduceByKey方法可以将相同key的value进行聚合操作
rdd = sc.parallelize([("d", 4), ("a", 2), ("f", 6), ("c", 3), ("h", 1)])
sorted_rdd = rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(sorted_rdd.collect())