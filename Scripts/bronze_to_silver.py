import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Glue Catalog (bronze table)
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="migration_catalog_db",
    table_name="crm"
)

# Convert to Spark dataframe
df = datasource.toDF()

# Example transformation
df_clean = df.dropDuplicates()

# Write to silver layer
df_clean.write.mode("overwrite").parquet(
    "s3://data-mig-set01/silver/crm/"
)

job.commit()