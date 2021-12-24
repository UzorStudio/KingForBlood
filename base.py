import pymongo
from bson import ObjectId
from datetime import datetime, timedelta, time


class Base():
    def __init__(self,classterMongo):
        self.classterMongo = classterMongo
        self.classter = pymongo.MongoClient(self.classterMongo)

    def getUsrs(self):
        db = self.classter["KingdomForBlood"]
        Kingdom = db["Kingdom"]

        cursor = Kingdom.find({})
        of = []
        for document in cursor:
            of.append(document)
        return of


    def getUsrById(self,usrId):
        db = self.classter["KingdomForBlood"]
        Kingdom = db["Kingdom"]
        return Kingdom.find_one({"usrId":usrId})


    def getUsrByUsrName(self,usrName):
        db = self.classter["KingdomForBlood"]
        Kingdom = db["Kingdom"]
        return Kingdom.find_one({"usrName":usrName})


    def setNameOfKingdom(self,usrId,KingdomName):
        db = self.classter["KingdomForBlood"]
        Kingdom = db["Kingdom"]
        Kingdom.update_one({"usrId":usrId},{"$set":{"KingdomName":KingdomName}})


    def setVerif(self,usrId,verif):
        db = self.classter["KingdomForBlood"]
        Kingdom = db["Kingdom"]
        Kingdom.update_one({"usrId":usrId},{"$set":{"verifikation":verif}})

    def postUser(self,usrName,usrId,KingdomName,kingdom,gold):
        db = self.classter["KingdomForBlood"]
        Kingdom = db["Kingdom"]
        post = {"usrId":usrId,
                "usrName":usrName,
                "kingdom":kingdom,
                "liver":3,
                "food":12,
                "warriors":0,
                "workers":0,
                "bilders":0,
                "gold":gold,
                "KingdomName":KingdomName,
                "homesize":kingdom["home"]*3,
                "verifikation":False
                }
        Kingdom.insert_one(post)

    def redaktKingdom(self,usrId,Type,Count):
        """in take the dict in the format {"type":0} or {"type":-1} or {"type":3}"""
        db = self.classter["KingdomForBlood"]
        Kingdom = db["Kingdom"]
        count = Kingdom.find_one({"usrId":usrId})["kingdom"][Type]

        Kingdom.update_one({"usrId": usrId},{"$set":{Type:count+Count}})
