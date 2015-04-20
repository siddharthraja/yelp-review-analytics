
# In[1]:

def topKeywords(response_ones,response_twos,response_threes,response_fours,response_fives):
    ones_keywords = []
    twos_keywords = []
    threes_keywords = []
    fours_keywords = []
    fives_keywords = []    
    if response_ones['status'] == 'OK':
        for keyword in response_ones['keywords']:
            if keyword['relevance'] > 0.6:
                if 'score' not in keyword['sentiment']:
                    ones_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type']})
                else:
                    ones_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type'],'sentiment score': keyword['sentiment']['score']})

    if response_twos['status'] == 'OK':
        for keyword in response_twos['keywords']:
            if keyword['relevance'] > 0.6:
                if 'score' not in keyword['sentiment']:
                    twos_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type']})
                else:
                    twos_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type'],'sentiment score': keyword['sentiment']['score']})

    if response_threes['status'] == 'OK': 
        for keyword in response_threes['keywords']:
            if keyword['relevance'] > 0.6:
                if 'score' not in keyword['sentiment']:
                    threes_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type']})
                else:
                    threes_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type'],'sentiment score': keyword['sentiment']['score']})

    if response_fours['status'] == 'OK':
        for keyword in response_fours['keywords']:
            if keyword['relevance'] > 0.6:
                if 'score' not in keyword['sentiment']:
                    fours_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type']})
                else:
                    fours_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type'],'sentiment score': keyword['sentiment']['score']})

    if response_fives['status'] == 'OK':            
        for keyword in response_fives['keywords']:
            if keyword['relevance'] > 0.6:
                if 'score' not in keyword['sentiment']:
                    fives_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type']})
                else:
                    fives_keywords.append({'keyword': keyword['text'].encode('utf-8'),'sentiment type': keyword['sentiment']['type'],'sentiment score': keyword['sentiment']['score']})
    
    return (ones_keywords,twos_keywords,threes_keywords,fours_keywords,fives_keywords)


# In[2]:

import json
from alchemyapi import AlchemyAPI

#load json file into json_data
with open("alchemy_input_data.json") as json_file:
    json_data = json.load(json_file)


# In[13]:

#load key into arrays that separate out business reviews by rating for a single category
alchemyapi = AlchemyAPI()
business_json = {}
for business in json_data.keys():
    business_ones = ""
    business_twos = ""
    business_threes = ""
    business_fours = ""
    business_fives = ""
    if "1" in json_data[business]:
        for item in json_data[business]["1"]:
            business_ones = business_ones + " " + item
    if "2" in json_data[business]:
        for item in json_data[business]["2"]:
            business_twos = business_twos + " " + item
    if "3" in json_data[business]:
        for item in json_data[business]["3"]:
            business_threes = business_threes + " " + item
    if "4" in json_data[business]:
        for item in json_data[business]["4"]:
            business_fours = business_fours + " " + item
    if "5" in json_data[business]:
        for item in json_data[business]["5"]:
            business_fives = business_fives + " " + item
            
    business_response_ones = alchemyapi.keywords("text", business_ones, {'sentiment': 1})
    business_response_twos = alchemyapi.keywords("text", business_twos, {'sentiment': 1})
    business_response_threes = alchemyapi.keywords("text", business_threes, {'sentiment': 1})
    business_response_fours = alchemyapi.keywords("text", business_fours, {'sentiment': 1})
    business_response_fives = alchemyapi.keywords("text", business_fives, {'sentiment': 1})
           
    data = {}
    data['1'] = business_response_ones
    data['2'] = business_response_twos
    data['3'] = business_response_threes
    data['4'] = business_response_fours
    data['5'] = business_response_fives
    
    business_json[business] = data
    
with open('data.json', 'w') as outfile:
    json.dump(business_json, outfile)


# In[4]:

ones = ""
twos = ""
threes = ""
fours = ""
fives = ""
#load key into arrays that separate out business reviews by rating for a single category
for business in json_data.keys():
    if "1" in json_data[business]:
        for item in json_data[business]["1"]:
            ones = ones + " " + item
    if "2" in json_data[business]:
        for item in json_data[business]["2"]:
            twos = twos + " " + item
    if "3" in json_data[business]:
        for item in json_data[business]["3"]:
            threes = threes + " " + item
    if "4" in json_data[business]:
        for item in json_data[business]["4"]:
            fours = fours + " " + item
    if "5" in json_data[business]:
        for item in json_data[business]["5"]:
            fives = fives + " " + item        


# In[104]:

#extract keywords from dictionary of {keyword,sentiment type,sentiment value}
ones = []
twos = []
threes = []
fours = []
fives = []

for keyword in ones_keywords:
    ones.append(keyword['keyword'])
    
for keyword in twos_keywords:
    twos.append(keyword['keyword'])
    
for keyword in threes_keywords:
    threes.append(keyword['keyword'])
    
for keyword in fours_keywords:
    fours.append(keyword['keyword'])
    
for keyword in fives_keywords:
    fives.append(keyword['keyword'])  

