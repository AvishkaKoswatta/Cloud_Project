start-dfs.sh
start-yarn.sh

hadoop fs -mkdir -p /input
hadoop fs -put /home/avishka/Cloud/Project/Data/clean_reviews.txt /input/
hdfs dfs -rm -r /output/review_analysis


hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -files mapper.py,reducer.py \
  -input /input/clean_reviews.txt \
  -output /output/review_analysis \
  -mapper mapper.py \
  -reducer reducer.py



to view results
hdfs dfs -ls /output/review_analysis
hdfs dfs -cat /output/review_analysis/part-00000 | less


#result analysing
#performance
#improve performance
