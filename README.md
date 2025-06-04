![Netflix Logo](https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg)

# Analysis of Netflix App Reviews from Google Play Store with Map Reduce

## This project performs analysis of Netflix app reviews using the Hadoop MapReduce framework. It processes a cleaned dataset containing user review words, and their associated ratings to compute the average rating per word in its category (positive, or negative).

## Source: Netflix Reviews from Google Play Store
https://www.kaggle.com/datasets/ashishkumarak/netflix-reviews-playstore-daily-updated 

## Input File: 
`clean_reviews.txt`

## Format: 
<sentiment> <word> <rating>

```bash
## Start Hadoop
start-dfs.sh
start-yarn.sh

## Upload Input File to HDFS
hadoop fs -mkdir -p /input
hadoop fs -put /home/avishka/Cloud/Project/Data/clean_reviews.txt /input/
hdfs dfs -rm -r /output/review_analysis

## Run MapReduce Job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -files mapper.py,reducer.py \
  -input /input/clean_reviews.txt \
  -output /output/review_analysis \
  -mapper mapper.py \
  -reducer reducer.py



## view results
hdfs dfs -ls /output/review_analysis
hdfs dfs -cat /output/review_analysis/part-00000 | less



