

# the reducer code for our mapreduce job
#from operator import itemgetter
import sys
total_score = 0
# STDIN Input
for l in sys.stdin:
    # input from the mapper is parsed
    key,score = l.split('\t', 1)
 # count is converted to int
    try:
       score = int(score)
    except ValueError:
       continue        # if score is not a number then ignore the line
    #Updating the total score

    total_score += score
print ('%s' % (total_score,))
