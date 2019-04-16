from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')

res = es.search(index="bole", doc_type="article")
print(res)

