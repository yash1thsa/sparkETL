from jobs import market_etl
from model import market_record
import datetime
from pyspark_test import assert_pyspark_df_equal
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType


class TestMarketETLJob:

    def test_transform_data(self, spark_session_builder):

        test_data = spark_session_builder.createDataFrame(
            [
                market_record.MarketRecord("5524", "1957", "Graduation", "Single", "58138", "0", "0", "04-09-2012", "58",
                                           "635", "88", "546", "172", "88", "88", "3", "8", "10", "4", "7", "0", "0", "0",
                                           "0", "0", "0", "3", "11", "1")
            ]
        )

        actual_df = market_etl._transform_data(test_data)
        expected_df = spark_session_builder.createDataFrame(
            [market_record.MarketOutputRecord(5524, "Graduation", "Single", datetime.date.today())]
        ).withColumn("id", col("id").cast(IntegerType()))

        assert_pyspark_df_equal(actual_df, expected_df)