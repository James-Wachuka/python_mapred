## INTRODUCTION
Using the mapreduce framework to score sentiments
## WHAT YOU NEED
This example requires that one has a basic understanding of hadoop and mapreduce framework
1. hadoop
2. python


This folder contains the map and reducer code for our mapreduce job
some text files have also been included for the mapreduce job.
you can use the following commands  for running this job on your hadoop file system

1. hadoop namenode -format                 # to format namenode

2. start-all                                # to start hadoop daemons
3. hadoop fs -mkdir /input                 # create an input directory
4. hadoop fs -put  opt/example.txt /input    #to put  a text file for mapreduce into the input directory
5. hadoop jar opt/hadoop-streaming-2.*.*.jar -file opt/mapper.py -mapper.py "python mapper.py" -file opt/reducer.py -reducer "python reducer.py" -input /input/example.txt -output sentimentscore

you must explicitly declare mapper and reducer files together with the input file and desired output name eg. sentimentscore

6. hadoop fs -cat /user/opt/sentimentscore/part-00000  # use this command to view your output

Also included are negative and positive words for use in scoring the sentiments

