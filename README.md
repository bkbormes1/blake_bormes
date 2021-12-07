Due Sunday
- README with links to all parts of pipeline
- explain business problem
- overview of our pipeline
- results and analysis
- detail API capabilities and limitations

# Project 3: Data Driven Bets - Alexandra Drossos, Courtney Smith, Blake Bormes, Austin Sanders

# Description of Problem

- Overview:

- [Data Source](https://sportsdata.io/developers/api-documentation/nfl#/fantasy/nfl-v3-projections-projected-player-game-stats-by-week-w-injuries-lineups-dfs-salaries)

- Research Questions:

# Tools Utilized

Google Cloud Platorm (GCP) - Establish Virtual Machine (VM) and infrastrucutre for
data pipeline.

Kafka - The queue for the files. Publish and consume messages for the dataset.

Zookeeper - The main node managing kafka.

Spark - Transforms the dataset to store it in a readable and queryable format.

Hadoop Distributed File System (HDFS) - Storage system for the readable tables.

Jupyter Notebook - Runs spark functions and queries; used for exploratory analysis. 

# Step-by-step Guide to Pipeline

1. Establish a VM through GCP
2. Create a docker file with required ports to run kafka, zookeeper, hadoop, and spark.
3. Download the JSON dataset 
```
curl -L -o assessment-attempts-20180128-121051-nested.json https://goo.gl/ME6hjp
```
4. Fire up docker container and check the logs to make sure everything is functioning properly.
5. Create a kafka topic ('education') to log all events related to the assessment dataset.
6. Publish and consume test messages through the education topic with Kafka.
7. Establish HDFS to later store the data in.
8. Create firewall rules in GCP to run spark through a jupyter notebook.
9. Launch spark and use the token with GCP VM's external IP to run jupyter notebook in browser.
10. Unnest JSON table and put in readable format.
11. Query data and create clean datasets for our data science team.
12. Store clean and ready tables in HDFS for queries.

# Links to Files

- [Project_3 Analysis Notebook]()
- [NFL API File]()
- [Spark Streaming File]()
- [Spark Batch File]()
- [Docker-Compose File]()

# Conclusion

