from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

#Create RDD using parallelize
data = [1,2,3,4,5,6,7,8,9,10,11,12]
rdd=spark.sparkContext.parallelize(data)
print('rdd',rdd.collect())

#Create RDD from a file
rdd2 = spark.sparkContext.textFile("/home/lordirah/PycharmProjects/pythonTutorials/sample_files/rdd_read.txt")
print('rdd2',rdd2.collect())

#Creating whole RDD
rdd3 = spark.sparkContext.wholeTextFiles("/home/lordirah/PycharmProjects/pythonTutorials/sample_files/rdd_read.txt")
print('rdd3',rdd3.collect())

#Empty RDD
rdd4 = spark.sparkContext.emptyRDD

#Empty RDD with partition
rdd5 = spark.sparkContext.parallelize([],10)
print('rdd5',rdd5.collect())

#Print the no of partitions
print("initial partition count:"+str(rdd5.getNumPartitions()))

#Repartition
reRdd5 = rdd5.repartition(4)
print("re-partition count:"+str(reRdd5.getNumPartitions()))

##RDD operations
rdd6 = spark.sparkContext.textFile("/home/lordirah/PycharmProjects/pythonTutorials/sample_files/rdd_read.txt")

#Flatmap and map
rdd7 = rdd6.flatMap(lambda x: x.split(" "))
rdd8 = rdd7.map(lambda x: (x,1))
rdd9 = rdd8.reduceByKey(lambda a,b: a+b)
rdd10 = rdd9.map(lambda x: (x[1],x[0])).sortByKey()
print(rdd10.collect())
rdd11 = rdd10.filter(lambda x : 'is' in x[1])
print(rdd11.collect())

##RDD Actions
data = [("Z", 1), ("A", 20), ("B", 30), ("C", 40), ("B", 30), ("B", 60)]
inputRDD = spark.sparkContext.parallelize(data)

listRdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5, 3, 2])

# aggregate
seqOp = (lambda x, y: x + y)
combOp = (lambda x, y: x + y)
agg = listRdd.aggregate(0, seqOp, combOp)
print(agg)  # output 20

# aggregate 2
seqOp2 = (lambda x, y: (x[0] + y, x[1] + 1))
combOp2 = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
agg2 = listRdd.aggregate((0, 0), seqOp2, combOp2)
print(agg2)  # output (20,7)

agg2 = listRdd.treeAggregate(0, seqOp, combOp)
print(agg2)  # output 20

# fold
from operator import add

foldRes = listRdd.fold(0, add)
print(foldRes)  # output 20

# reduce
redRes = listRdd.reduce(add)
print(redRes)  # output 20

# treeReduce. This is similar to reduce
add = lambda x, y: x + y
redRes = listRdd.treeReduce(add)
print(redRes)  # output 20

# Collect
data = listRdd.collect()
print(data)

# count, countApprox, countApproxDistinct
print("Count : " + str(listRdd.count()))
# Output: Count : 20
print("countApprox : " + str(listRdd.countApprox(1200)))
# Output: countApprox : (final: [7.000, 7.000])
print("countApproxDistinct : " + str(listRdd.countApproxDistinct()))
# Output: countApproxDistinct : 5
print("countApproxDistinct : " + str(inputRDD.countApproxDistinct()))
# Output: countApproxDistinct : 5

# countByValue, countByValueApprox
print("countByValue :  " + str(listRdd.countByValue()))

# first
print("first :  " + str(listRdd.first()))
# Output: first :  1
print("first :  " + str(inputRDD.first()))
# Output: first :  (Z,1)

# top
print("top : " + str(listRdd.top(2)))
# Output: take : 5,4
print("top : " + str(inputRDD.top(2)))
# Output: take : (Z,1),(C,40)

# min
print("min :  " + str(listRdd.min()))
# Output: min :  1
print("min :  " + str(inputRDD.min()))
# Output: min :  (A,20)

# max
print("max :  " + str(listRdd.max()))
# Output: max :  5
print("max :  " + str(inputRDD.max()))
# Output: max :  (Z,1)

#write to file
inputRDD.saveAsTextFile("/home/lordirah/PycharmProjects/pythonTutorials/sample_files/wordcount")

# take, takeOrdered, takeSample
print("take : " + str(listRdd.take(2)))
# Output: take : 1,2
print("takeOrdered : " + str(listRdd.takeOrdered(2)))
# Output: takeOrdered : 1,2
print("take : " + str(listRdd.takeSample()))