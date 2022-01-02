from pyspark import SparkContext, SparkConf
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, HiveContext

sparkSession = (SparkSession
                .builder
                .appName('example-pyspark-read-and-write-from-hive')
                .config("hive.metastore.uris", "thrift://localhost:9083", conf=SparkConf())
                .enableHiveSupport()
                .getOrCreate()
                )

emp_df = sparkSession.sql('select emp_no,first_name,last_name from employees.employees')
sal_df = sparkSession.sql('select emp_no,salary from employees.salaries where to_date = \'9999-01-01\'')
#Joins
#emp_sal_details_df = emp_df.alias('a').join(sal_df.alias('b'),emp_df.emp_no == sal_df.emp_no, 'inner') #Use this in case different column name is used in the join
emp_sal_details_df = emp_df.alias('a').join(sal_df.alias('b'),'emp_no', 'inner').show() #Use this in case same column name is used in the join
#emp_sal_details_df.select('first_name','last_name','salary').show()
