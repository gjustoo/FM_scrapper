from db.MongoDBConnection import MongoDBConnection

from model.FMQuery import FMQuery


class SearchQueryRepo:
    def __init__(self):
        self.client = MongoDBConnection.getInstance().client
        self.db = self.client.db_name
        self.collection_name = "searchQueries"
        self.collection = self.db[self.collection_name]
        
    def insert_one(self, search_query: FMQuery):
        self.collection.insert_one(search_query.to_dict())
    
    def get_all(self):
        return self.collection.find()
    
    def get_by_query(self, query: str):
        return self.collection.find_one({"query": query})
    
    def insert_multiple(self, search_queries: list[FMQuery]):
        self.collection.insert_many([query.to_dict() for query in search_queries])
        
    def is_not_empty(self):
        return self.collection.count_documents({}) > 0