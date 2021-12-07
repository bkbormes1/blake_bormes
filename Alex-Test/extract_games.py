#!/usr/bin/env python
"""Extract events from kafka and write them to hdfs
"""

import json
import pandas as pd
from pyspark.sql.functions import explode, split
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, TimestampType
import warnings

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
        .option("subscribe", "season") \
        .option("startingOffsets", "earliest") \
        .option("endingOffsets", "latest") \
        .load()
    
    games = raw_games.select(raw_games.value.cast('string'))
    
    final_schema = StructType([StructField('GameKey', StringType(), True),
                     StructField('Week', StringType(), True),
                     StructField('AwayTeam', StringType(), True),
                     StructField('AwayScore', IntegerType(), True),
                     StructField('HomeTeam', StringType(), True),
                     StructField('HomeScore', IntegerType(), True),
                     StructField('PointSpread', FloatType(), True),
                     StructField('OverUnder', FloatType(), True),
                     StructField('AwayTeamMoneyLine', IntegerType(), True),
                     StructField('HomeTeamMoneyLine', IntegerType(), True)])
    
    games_df = games.rdd.map(lambda x: json.loads(x.value)).toDF(schema=final_schema)

    games_df \
        .write \
        .parquet("/tmp/season")
    

if __name__ == "__main__":
    main()
