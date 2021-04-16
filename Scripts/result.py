from pywebio.input import *
from pywebio.output import *

from pymongo import MongoClient

client = MongoClient('localhost',port =27017)

db = client.Voting_records

db_collection = db.Voters

bjp=0
cng=0
other=0

for x in db_collection.find():
    for key, value in x.items():
        if key == 'vote_for':
            if value == 'BJP':
                bjp+=1

            elif value == 'CNG':
                cng+=1


            else:
                other+=1        

if bjp>cng:
    style(put_text("WINNER is BJP.."),'color:orange')

else:
    put_text("WINNER is CNG..")    