#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""

import json
import pandas as pd
from pyspark.sql.functions import explode, split, from_json
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, TimestampType
import warnings

def game_schema():
    """
    root
    |-- Accept: string (nullable = true)
    |-- Host: string (nullable = true)
    |-- User-Agent: string (nullable = true)
    |-- event_type: string (nullable = true)
    |-- timestamp: string (nullable = true)
    """
    return StructType([
        StructField('GameKey', StringType(), True),
        StructField('Week', StringType(), True),
        StructField('AwayTeam', StringType(), True),
        StructField('AwayScore', IntegerType(), True),
        StructField('HomeTeam', StringType(), True),
        StructField('HomeScore', IntegerType(), True),
        StructField('PointSpread', FloatType(), True),
        StructField('OverUnder', FloatType(), True),
        StructField('AwayTeamMoneyLine', IntegerType(), True),
        StructField('HomeTeamMoneyLine', IntegerType(), True)])
  
def main():
    """main
    """
    spark = SparkSession \
        .builder \
        .appName("ExtractEventsJob") \
        .getOrCreate()

    raw_games = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:29092") \
        .option("subscribe", "games") \
        .load()
    
    the_games = raw_games.select(raw_games.value.cast('string')) 
    
# Change to every 6 minutes to match our loop
    sink = the_games \
        .writeStream \
        .format("parquet") \
        .option("checkpointLocation", "/tmp/checkpoints_for_games") \
        .option("path", "/tmp/games") \
        .trigger(processingTime="30 seconds") \
        .start()

    sink.awaitTermination()


if __name__ == "__main__":
    main()
