import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
sc = spark.sparkContext
sc.addFile("D:\My Files\Codes\python\spark\scenarios\load_data.py")

from load_data import load_data

regions, countries, locations, jobs, departments, employees, dependents = load_data(spark)

#employee_id,(full name),jobtitle,dependent fullname, department name, city, country, region
#employee name and corresponding manager name, whose salary is greater than 4000
#job type, years as different columns and sum up the salary
#Find for which job type there is no employees
#New column flag (high/low) if salary is less than 10000

#Explode array values
#udf -> implement python operation to a column value

#Questions
#Spark optimization
#Memory concepts
#Joins types in spark
#Broadcasting
#Spark session vs spark context

