from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "E:/Python/python3.11.7/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["itheima itcast 6666", "itheima itheima itecast", "python itheima"])

# 需求，将RDD数据里面的每一个单词提取出来
# flatMap方法可以将RDD里面的每一个元素进行拆分，拆分之后的结果会放到一个新的RDD里面
# rdd2 = rdd.map(lambda x: x.split(" "))

rdd2 = rdd.flatMap(lambda data: data.split(" "))
print(rdd2.collect())



