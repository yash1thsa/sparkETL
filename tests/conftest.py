import pytest
from pyspark.sql import SparkSession


@pytest.fixture
def spark_session_builder():
    return SparkSession.builder \
        .master("local") \
        .appName("test") \
        .getOrCreate()
