# -*- coding: utf-8 -*-

from datetime import datetime
from elasticsearch_dsl import Document, Date, Nested, Boolean, \
analyzer, Completion, Keyword, Text

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalysis
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalysis):
    def get_analysis_definition(self):
        return {}
        
ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(Document):
    suggest   = Completion(analyzer=ik_analyzer)
    title     = Text(analyzer="ik_max_word")
    published = Date()
    abstract  = Text(analyzer="ik_max_word")
    tag       = Text(analyzer="ik_max_word")
    link      = Keyword()

    class Index:
        name = "bole"
        settings = {
            "number_of_shards":5,
        }

if __name__ == "__main__":
    ArticleType.init()
