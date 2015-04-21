# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
import operator

# <codecell>

json_data = open('yelp-data/data.json')
data = json.loads(json_data.read())

# <codecell>

keywords = {}
for business in data:
    for rating in range(1,6):
        if 'keywords' in data[business][str(rating)]:
            for k in data[business][str(rating)]['keywords']:
                #print k
                if k['text'] not in keywords:
                    keywords[k['text']] = [{"business_id":business, "relevance":k['relevance']}]
                else:
                    keywords[k['text']].append({"business_id":business, "relevance":k['relevance']})
    

# <codecell>

file_writer = open('categories_keywords.json','w')
file_writer.write(json.dumps(keywords))

# <codecell>


