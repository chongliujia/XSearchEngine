#-*- coding:utf-8 -*-
import json
from elasticsearch import Elasticsearch
import elasticsearch.helpers

es = Elasticsearch("localhost:9200")
package = {}
row = {}
num = 0
file = open('bole.json', 'r', encoding='utf-8')
for k in file:
    f = json.loads(k)
    num = num + 1
    print(f['title'])
    row = {
        "title":f['title'],
        "abstract":f['abstract'],
        "tag":f['tag'],
        "link":f['link'],
        "published":f['published']
    }
    package.update(row)

actions = {
    '_index': "bole",
    '_type':"article",
    '_source':d

}



elasticsearch.helpers.bulk(es, actions)

