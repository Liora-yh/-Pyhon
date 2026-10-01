from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "E:/Python/python3.11.7/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

rdd2 = sc.parallelize(range(1, 10))
print(rdd2.reduce(lambda a, b: a + b))

take_list = rdd.take(3)
print(take_list)

num_count = rdd.count()
print(num_count)

rdd.saveAsTextFile("output/rdd_output.txt")
# 输出到文件中