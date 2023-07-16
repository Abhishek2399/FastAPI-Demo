"""

Here we will use the motor library to interact with the mongo database,
here we will have the functions that will communicate with the database

"""
from model import Todo
# this is the mongoDb driver
import motor.motor_asyncio as motor_async
from pymongo.server_api import ServerApi


# client = motor_async.AsyncIOMotorClient('mongodb://localhost:27017') # for connecting to the database hosted locally

uri = "mongodb+srv://AbhiBhovar:Abhi2399@cluster0.dnndhdq.mongodb.net/"
client = motor_async.AsyncIOMotorClient(uri, server_api=ServerApi('1')) 

# we will have a database 'TodoList'
db = client.TodoList


# inside the database we have one collection of 'todo'
collection = db.todo


# creating the functions that we will be using to query data

# query single item based on title
async def fetch_one_todo(title):
    document = await collection.find_one({'title' : title})
    return document


# function that will return a list of all the tasks  
async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


# function that will create single todo
async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


# function that will update single todo
async def update_todo(title, desc):
    await collection.update_one({'title' : title}, {'$set' : {'description' : desc}}) # update_one(filter, data)
    document = await collection.find_one({'title' : title})
    return document


# function that will remove todo
async def remove_todo(title):
    await collection.delete_one({'title' : title})
    return True












