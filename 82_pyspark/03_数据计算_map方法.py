from pyspark import SparkConf, SparkContext

import os
os.environ["PYSPARK_PYTHON"] = "E:/Python/python3.11.7/python.exe"


conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 通过map方法讲全部数据都乘以10
def func(data):
    return data * 10

rdd2 = rdd.map(func)

print(rdd2.collect())

# 链式调用
rdd3 = rdd.map(lambda data: data * 10)
print(rdd3.collect())



