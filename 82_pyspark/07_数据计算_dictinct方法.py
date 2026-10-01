from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "E:/Python/python3.11.7/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 3, 8, 4, 2, 3, 7, 5, 6, 8, 9, 10])

# 去重
distinct_rdd = rdd.distinct()
print(distinct_rdd.collect())


