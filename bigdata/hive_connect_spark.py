from pyspark import SparkContext, SparkConf
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, HiveContext
"""
SparkSession ss = SparkSession
.builder()
.appName(" Hive example")
.config("hive.metastore.uris", "thrift://localhost:9083")
.enableHiveSupport()
.getOrCreate();
"""

sparkSession = (SparkSession
                .builder
                .appName('example-pyspark-read-and-write-from-hive')
                .config("hive.metastore.uris", "thrift://localhost:9083", conf=SparkConf())
                .enableHiveSupport()
                .getOrCreate()
                )

emp_df = sparkSession.sql('select count(*) from employees.employees')
emp_df.show()
print(emp_df.show())
