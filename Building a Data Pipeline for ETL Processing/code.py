# Import necessary PySpark libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder \
    .appName("SimpleDataPipeline") \
    .getOrCreate()

# Load data from a CSV file into a DataFrame
input_file_path = "hdfs://path/to/input_file.csv"  # Update the path with your actual input file path
df = spark.read.csv(input_file_path, header=True)  # Assuming the CSV file has a header

# Perform data transformation - For example, filtering out rows where a specific column value is null
transformed_df = df.filter(col("column_name").isNotNull())

# Write the transformed data back to a new CSV file
output_file_path = "hdfs://path/to/output_file.csv"  # Update the path with your desired output file path
transformed_df.write.csv(output_file_path, header=True, mode="overwrite")

# Stop the Spark session
spark.stop()
