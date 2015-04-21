# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json

# <codecell>

categories = {}
json_data = open('yelp-data/yelp_academic_dataset_business.json')
#data = json.load(json_data)
#file_writer = open('yelp-data/yelp_business_categories.json')
for d in json_data:
    data = json.loads(d)
    print data["business_id"]
    print data['stars']
    print data['full_address'].split()[-3].strip().strip(',')
    for category in data['categories']:
        if category in categories:
            categories[category].append({"business_id":data["business_id"], "name": data["name"],"city":data['full_address'].split()[-3].strip().strip(','),"stars":data['stars']})
        else:
            categories[category]=[{"business_id":data["business_id"], "name": data["name"], "city":data['full_address'].split()[-3].strip().strip(','), "stars":data['stars']}]  
    #break
                                        

# <codecell>

json.dump(categories, open('yelp_business_categories.json', 'wb'))

# <codecell>


