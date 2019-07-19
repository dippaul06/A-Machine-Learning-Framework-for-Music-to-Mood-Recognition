import csv


#with open('/Users/dippaul/Downloads/test1.csv','r') as csvinput:
    #with open('/Users/dippaul/Downloads/test2.csv', 'w') as csvoutput:
     #   writer = csv.writer(csvoutput, lineterminator='\n')
      #  reader = csv.reader(csvinput)

row = ['e','cse','8']

with open('/Users/dippaul/Downloads/test2.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

    csvFile.close()

