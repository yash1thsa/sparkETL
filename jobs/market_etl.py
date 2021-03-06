from pyspark.sql.functions import current_date, col
from pyspark.sql.types import IntegerType


def _extract_data(spark, config):
    return spark.read.option("header", "True")\
        .option("delimiter", "\t")\
        .csv(config['source_data_path'])


def _transform_data(data_df):
    final_df = data_df.withColumn("snapshot_dt", current_date())\
        .select(col("ID").cast(IntegerType()).alias("id"),
                col("Education").alias("education"),
                col("Marital_Status").alias("marital_status"),
                col("snapshot_dt"))
    return final_df


def _load_data(config, final_df):
    final_df\
        .repartition(1)\
        .write \
        .partitionBy("snapshot_dt")\
        .mode("overwrite")\
        .format("parquet")\
        .save(config['target_data_path'])


def run_job(spark, config):
    _load_data(config, _transform_data(_extract_data(spark, config)))