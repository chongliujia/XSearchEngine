import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(['localhost'], port=9200)
actions = []
file = open('bole.json', 'r', encoding='utf-8')
i = 1
for k in file:
    f = json.loads(k)
    action = {
        "_index":"bole",
        "_type":"article",
        "_id":i,
        "_source":{
            "title":f['title'],
            "abstract":f['abstract'],
            "tag":f['tag'],
            "link":f['link'],
            "published":f['published']
        }
    }
    i = i + 1
    actions.append(action)


if (len(actions) > 0):
    helpers.bulk(es, actions)

