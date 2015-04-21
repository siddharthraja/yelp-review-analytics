# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
import operator

# <codecell>

json_data = open('yelp-data/data.json')
data = json.loads(json_data.read())

# <codecell>

print len(data)

# <codecell>

for d in data:
    filename = "vis_data/"+d + ".csv"
    file_writer = open(filename, 'w')
    file_writer.write('rating, keyword, relevance, bucket\n')
    print d
    for rating in range(1,6):        
        if "keywords" in data[d][str(rating)]:
            keywords = []
            for k in data[d][str(rating)]["keywords"]:
                if "sentiment" in k:
                    if k["sentiment"]["type"] != "neutral":
                        keywords.append((k["text"],k["relevance"],(int(float(k["sentiment"]["score"]) * 100)/20 )+ 5,k["sentiment"]["type"]))
                    else:
                        keywords.append((k["text"],k["relevance"],0,k["sentiment"]["type"]))
                else:
                    keywords.append((k["text"],k["relevance"],5,"none"))
            buckets = {i: [] for i in range(0,10)}
            for keyword in keywords:
                if keyword[3] != 'none':
                    buckets[keyword[2]].append(keyword)
            #print buckets.keys()
            for i in range(0,10):
                #print i
                if buckets[i] != []:
                    buckets[i].sort(key=operator.itemgetter(1), reverse=True)
                    if len(buckets[i]) > 0:
                        print buckets[i][0][0]
                        file_writer.write(str(rating) + ', ' +buckets[i][0][0].encode('utf-8') + ", " + str(buckets[i][0][1]) + ", " + str(buckets[i][0][2]) + "\n")
                    if len(buckets[i]) > 1:
                        print buckets[i][1][0]
                        file_writer.write(str(rating) + ', ' + buckets[i][1][0].encode('utf-8')+ ", " + str(buckets[i][1][1]) + ", " + str(buckets[i][1][2]) + "\n")
                    #print str(rating) + ', ' +buckets[i][0][0] + ", " + str(buckets[i][0][1]) + ", " + str(buckets[i][0][2]) + "\n"
            #print buckets[8]
            #print len(data[d][str(rating)]["keywords"])
            #keywords.sort(key=operator.itemgetter(1))
            #print keywords
        else:
            print "none"
    #break
    file_writer.close()    

# <codecell>

3

# <codecell>


