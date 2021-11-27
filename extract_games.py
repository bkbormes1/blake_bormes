#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""

import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf

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
    final_schema = StructType([StructField('GameKey', StringType(), True),StructField('AwayTeam', StringType(), True),StructField('HomeTeam', StringType(), True)])
    games_df = games.rdd.map(lambda x: json.loads(x.value)).toDF(schema=final_schema)

    games_df \
        .write \
        .parquet("/tmp/extracted_games")


if __name__ == "__main__":
    main()
