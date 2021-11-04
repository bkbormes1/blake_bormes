#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""

import json
from pyspark.sql import SparkSession


def main():
    """main
    """
    spark = SparkSession \
        .builder \
        .appName("ExtractEventsJob") \
        .getOrCreate()

    raw_games = spark \
        .read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:29092") \
        .option("subscribe", "games") \
        .option("startingOffsets", "earliest") \
        .option("endingOffsets", "latest") \
        .load()
    
# Adjust as necessary to properly format our table
    games = raw_games.select(raw_games.value.cast('string'))
    extracted_games = games.rdd.map(lambda x: json.loads(x.value)).toDF()

    extracted_games \
        .write \
        .parquet("/tmp/extracted_games")


if __name__ == "__main__":
    main()
