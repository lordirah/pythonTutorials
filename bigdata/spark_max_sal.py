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


sal_df = sparkSession.sql("select * from employees.salaries")
employees = sparkSession.sql("select * from employees.employees")

sal_df = sal_df.selectExpr("emp_no","salary","row_number() over (partition by emp_no order by salary desc) as rnk")
sal_df = sal_df.filter("rnk = 1").drop("rnk").selectExpr("*","emp_no as emp_emp_no").drop("emp_no")
sal_df.show()
sal_df.count()

final = sal_df.join(employees,sal_df.emp_emp_no == employees.emp_no,'inner').select(sal_df.emp_emp_no,sal_df.salary,employees.first_name,employees.last_name)

sparkSession.sql("create table employees.employees_max_sal (emp_no string, salary int, first_name string,last_name string)")

final.write.mode('overwrite').format('csv').insertInto("employees.employees_max_sal") #overwrite

final.count()
