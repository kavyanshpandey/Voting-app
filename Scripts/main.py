from pywebio.input import *
from pywebio.output import *
from pymongo import MongoClient
import os
from pathlib import Path
from dotenv import load_dotenv

# Get the base directory
basepath = Path()
basedir = str(basepath.cwd())


# Load the environment variables
envars = basepath.cwd() / '.env'
load_dotenv(envars)


# Read an environment variable.
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

#Setup database connectivity
client = MongoClient(HOST,PORT)
db = client.User_records
coll = db.users_vote
    


def voting():
    name = input('Enter your name', type="text",required=True)
    age = input('Enter your age', type=NUMBER,required=True)

    if age >=18:
        put_text('Check your details..')

        put_table([['NAME','AGE'],
        [name, age]])

        check = checkbox(options = ['All details are correct.'])

        if check:
            selction = radio("Select your party",['Congress','BJP','AAP'])

            records = {
                'name':name,
                'age':age,
                'vote_for': selction
            }
            coll.insert_one(records)

            
            put_text('Thanks, Your response has been recorded.')

            keep_voting = radio('Keep Voting', ['Yes', 'No'])

            if keep_voting == 'Yes':
                voting()


            else:
                return style(put_text('Voting has been ended, We will announce the result soon..'),'color:green')    

    else:
        style(put_text('You are not eligible for voting..'),'color:red')

        keep_voting = radio('Keep Voting', ['Yes', 'No'])

        if keep_voting == 'Yes':
            voting()


        else:
            return style(put_text('Voting has been ended, We will announce the result soon..'),'color:green')

voting()
