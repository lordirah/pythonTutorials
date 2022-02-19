import findspark
findspark.init()
from pyspark.sql import SparkSession, DataFrame
from pyspark import SparkContext

def create_session():
    spark = SparkSession.builder.appName('Netflix').getOrCreate()
    sc = spark.sparkContext
    sc.addFile("util.py")
    return spark,sc

def read_data(spark:SparkSession) -> DataFrame:
    df = spark.read.csv("/mnt/d/My Files/Codes/python/pythonTutorials/bigdata/netflix/netflix_titles.csv",header = True)
    return df

def main():
    spark,sc = create_session()
    import util
    cols = ['show_id','type','title']
    final_df = util.specific_select(read_data(spark), cols)
    final_df.show(10, truncate = False)    
if __name__ == "__main__":
    main()
