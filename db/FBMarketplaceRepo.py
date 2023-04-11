from db.MongoDBConnection import MongoDBConnection

from model.CarAD import CarAD


class FBMarketplaceRepo:
    def __init__(self):
        self.client = MongoDBConnection.getInstance().client
        self.db = self.client.db_name
        self.collection_name = "fbMarketplace"
        self.collection = self.db[self.collection_name]

    def insert_car_ad(self, car_ad: CarAD):
        self.collection.insert_one(car_ad)

    def get_car_ads(self):
        return self.collection.find()

    def get_car_ad_by_uid(self, uid):
        return self.collection.find_one({"uid": uid})

    def insert_car_ads(self, car_ads):
        self.collection.insert_many(car_ads)

    def exists_car_ad(self, car_ad: CarAD):
        return self.collection.find_one({"uid": car_ad.uid}) != None

    def update_car_ad(self, car_ad: CarAD):
        return self.collection.update_one({"uid": car_ad.uid}, {"$set": car_ad.__dict__})

    def insert_or_update_car_ad(self, car_ad: CarAD):
        if self.exists_car_ad(car_ad):
            self.update_car_ad(car_ad)
        else:
            self.insert_car_ad(car_ad)
