from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql import SparkSession

dataDF = [(('James','','Smith'),'1991-04-01','M',3000),
  (('Michael','Rose',''),'2000-05-19','M',4000),
  (('Robert','','Williams'),'1978-09-05','M',4000),
  (('Maria','Anne','Jones'),'1967-12-01','F',4000),
  (('Jen','Mary','Brown'),'1980-02-17','F',-1)
]

schema = StructType([
        StructField('name', StructType([
             StructField('firstname', StringType(), True),
             StructField('middlename', StringType(), True),
             StructField('lastname', StringType(), True)
             ])),
         StructField('dob', StringType(), True),
         StructField('gender', StringType(), True),
         StructField('gender1', IntegerType(), True)
         ])

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
df = spark.createDataFrame(data = dataDF, schema = schema)
df.printSchema()
#df.withColumnRenamed("dob","DateOfBirth").printSchema()
#df.withColumn("salary",col("salary")*100).show()
#df.sort("department","state").show(truncate=False)
#df2 = df.select(df.name,explode(df.knownLanguages))
#df3 = df.select(df.name,explode(df.properties))
#df2 = spark.read.option("header",True) .csv("/tmp/resources/zipcodes.csv")
#df2.write.options(header='True', delimiter=',').csv("/tmp/spark_output/zipcodes")
#df.groupBy("department").sum("salary").show(truncate=False)

df.filter(df.gender == 'M').show(truncate = False)
