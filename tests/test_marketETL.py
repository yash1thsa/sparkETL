import pandas as pd
from jobs import marketETL


class TestMaketETLJob:
    def test_transform_data(self, spark_session):

        test_data = spark_session.createDataFrame(
            [
                ()
            ]
        )