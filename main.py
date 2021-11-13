from pyspark.sql import SparkSession
import json
import importlib
import argparse


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    return parser.parse_args()


def main():
    args = parse_argument()

    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    spark = SparkSession.builder \
        .master("local") \
        .appName(config['app_name']) \
        .getOrCreate()

    job_module = importlib.import_module(f"jobs.{args.job}")
    job_module.run_job(spark, config)


if __name__ == '__main__':
    main()

