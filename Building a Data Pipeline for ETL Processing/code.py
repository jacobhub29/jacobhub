# Import necessary PySpark and pyspark-bigquery libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark_bigquery import saveAsBigQuery

# Create a Spark session
spark = SparkSession.builder \
    .appName("DataPipelineToBigQuery") \
    .getOrCreate()

# Load data from a CSV file into a DataFrame
input_file_path = "hdfs://path/to/input_file.csv"  # Update the path with your actual input file path
df = spark.read.csv(input_file_path, header=True)  # Assuming the CSV file has a header

# Perform data transformation - For example, filtering out rows where a specific column value is not null
transformed_df = df.filter(col("column_name").isNotNull())

# Define the BigQuery output table name
output_table_name = "your_project_id.dataset.table_name"  # Update with your BigQuery table details

# Write the transformed data to a BigQuery table
transformed_df.write.format('bigquery') \
    .option('table', output_table_name) \
    .save()

# Stop the Spark session
spark.stop()
