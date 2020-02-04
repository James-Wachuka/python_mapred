This folder contains the map and reducer code for our mapreduce job
some text files have also been included for the mapreduce job
you can use the following commands  for running this job on your hadoop file system

hadoop namenode -format                 # to format namenode
start-all                                # to start hadoop daemons
hadoop fs -mkdir /input                 # create an input directory
hadoop fs -put  opt/exmaple.txt /input    #to put  a text file for mapreduce into the input directory
hadoop jar opt/hadoop-streaming-2.*.*.jar -file opt/mapper.py -mapper.py "python mapper.py" -file opt/reducer.py -reducer "python reducer.py" -input /input/example.txt -output sentimentscore

you must explicitly declare mapper and reducer files together with the input file and desired output name eg. sentimentscore

hadoop fs -cat /user/opt/sentimentscore/part-00000  # use this command to view your output
