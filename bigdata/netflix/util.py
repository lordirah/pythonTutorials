from pyspark.sql import *

def specific_select(inp_df, cols) -> DataFrame:
    selected_df = inp_df.select(cols)
    return selected_df
