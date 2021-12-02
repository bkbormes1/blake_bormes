Due Sunday
- README with links to all parts of pipeline
- explain business problem
- overview of our pipeline
- results and analysis


# W205_Project_3

https://sportsdata.io/developers/api-documentation/nfl#/fantasy/nfl-v3-projections-projected-player-game-stats-by-week-w-injuries-lineups-dfs-salaries


# Notes
Pipeline:
Events-Stream-Queue-Store
- create script (can be bash) to run kafka/pyspark set up in terminal ('doing the jobs')
- py scripts will GET data, filter into table, save to Hadoop
- run script in terminal using 'exec spark, spark-submit'

Query-Analysis
- use notebook for visualizations and exploratory analysis (query side)

Next Steps
- limit columns for only what we want to use in analysis (scores, teams, betting info, other ideas?). Make our table queryable
- we need to think about our 'research questions' - what will we use this pipeline for


# Project 3: Understanding User Behavior

## This is a team project, up to 4 people per team. At Week 14, you will present your project to the class.

- You have two options

### 1. Option 1: Mock data

  - You're a data scientist at a game development company  

  - Your latest mobile game has two events you're interested in tracking: `buy a
    sword` & `join guild`

  - Each has metadata characterstic of such events (i.e., sword type, guild name,
    etc)

### 2. Option 2: Real Data

  - Use your favorite API to connect to real data (Finance, News API, etc.)

  - Define your problem and your solution.

## Tasks

- Instrument your API server to log events to Kafka (Alex)

- Assemble a data pipeline to catch these events: use Spark streaming to filter
  select event types from Kafka, land them into HDFS/parquet to make them
  available for analysis using Presto. (Austin)

- Use Apache Bench to generate test data for your pipeline. (Blake)

- Construct some research questions from the data (Alex)

- Conduct some basic analysis on the events - queries/visualizations in a notebook (Courtney)

- Produce an analytics report where you provide a description of your pipeline. (All)
- Produce a presentation for Week 14 - in 3 weeks (All)


Use a notebook or markdown to present your queries and findings. Remember that this
notebook should be appropriate for presentation to someone else in your
business who needs to act on your recommendations. 

It's understood that events in this pipeline are _generated_ events which make
them hard to connect to _actual_ business decisions.  However, we'd like
students to demonstrate an ability to plumb this pipeline end-to-end, which
includes initially generating test data as well as submitting a notebook-based
report of at least simple event analytics.

If you are doing option 1, analytics are a small part of your final product. If you are doing Option 2, you can focus more on analytics and visualizations.

## Options

There are plenty of advanced options for this project.  Here are some ways to
take your project further than just the basics we'll cover in class:

- Generate and filter more types of events.  There are plenty of other things
  you might capture as events.
  
- Enhance the API to use additional http verbs such as `POST` or `DELETE` as
  well as additionally accept _parameters_ for events.

- Connect a user-keyed storage engine such as Redis or Cassandra up to Spark so
  you can track user state during gameplay (e.g., user's inventory or health)
  
---

#### GitHub Procedures

Important:  In w205, please never merge your assignment branch to the master branch. 

Using the git command line: clone down the repo, leave the master branch untouched, create an assignment branch, and move to that branch:
- Open a linux command line to your virtual machine and be sure you are logged in as jupyter.
- Create a ~/w205 directory if it does not already exist `mkdir ~/w205`
- Change directory into the ~/w205 directory `cd ~/w205`
- Clone down your repo `git clone <https url for your repo>`
- Change directory into the repo `cd <repo name>`
- Create an assignment branch `git branch assignment`
- Checkout the assignment branch `git checkout assignment`

The previous steps only need to be done once.  Once you your clone is on the assignment branch it will remain on that branch unless you checkout another branch.

The project workflow follows this pattern, which may be repeated as many times as needed.  In fact it's best to do this frequently as it saves your work into GitHub in case your virtual machine becomes corrupt:
- Make changes to existing files as needed.
- Add new files as needed
- Stage modified files `git add <filename>`
- Commit staged files `git commit -m "<meaningful comment about your changes>"`
- Push the commit on your assignment branch from your clone to GitHub `git push origin assignment`

Once you are done, go to the GitHub web interface and create a pull request comparing the assignment branch to the master branch.  Add your instructor, and only your instructor, as the reviewer.  The date and time stamp of the pull request is considered the submission time for late penalties. 

If you decide to make more changes after you have created a pull request, you can simply close the pull request (without merge!), make more changes, stage, commit, push, and create a final pull request when you are done.  Note that the last data and time stamp of the last pull request will be considered the submission time for late penalties.

Make sure you receive the emails related to your repository! Your project feedback will be given as comment on the pull request. When you receive the feedback, you can address problems or simply comment that you have read the feedback. 
AFTER receiving and answering the feedback, merge you PR to master. Your project only counts as complete once this is done.
