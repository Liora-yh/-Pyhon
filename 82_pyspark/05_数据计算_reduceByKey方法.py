from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "E:/Python/python3.11.7/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男', 99), ('男', 70), ('女', 99), ('女', 89)])

# 求男生和女生两个组的成绩之和
result = rdd.reduceByKey(lambda a, b: a + b)
print(result.collect())


