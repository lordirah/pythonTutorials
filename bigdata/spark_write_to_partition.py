import findspark
findspark.init()


from pyspark.sql.types import StructType,StructField, StringType, IntegerType
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
sparkSession.conf.set("hive.exec.dynamic.partition","true")
sparkSession.conf.set("hive.exec.dynamic.partition.mode","nonstrict")

test = [(2,'test1','test1',20)]
schema = StructType([
            StructField('emp_no',IntegerType(),True),
            StructField('from_date',StringType(),True),
            StructField('to_date',StringType(),True),
            StructField('dept_no',IntegerType(),True)
            ])

df = sparkSession.createDataFrame(data=test,schema=schema)
df.show()

df.coalesce(1).write.mode('append').format('csv').insertInto("employees.dept_emp_ext") #overwrite

