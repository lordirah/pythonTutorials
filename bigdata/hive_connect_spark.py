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

df_load = sparkSession.sql('select count(*) from employees.titles')
df_load.show()
print(df_load.show())
