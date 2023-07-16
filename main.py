from fastapi import FastAPI, HTTPException 
# CORS is used when we want two apps deployed on different ports to communicate with each other
from fastapi.middleware.cors import CORSMiddleware 
from model import Todo
import database as db

# HTTPException to handle errors and exception

# creating aan app 
app = FastAPI()


# adding the origin of React app
origins = ['https://localhost:3000']


# adding the middleware
app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_methods = ['*'],
        allow_headers = ['*'],
        allow_credentials = True
    )


@app.get("/")
def index():
    return {"Tech" : "FARM Stack"}


# to get all the tasks from todo list
@app.get("/api/todo")
async def get_todo_list():
    response = await db.fetch_all_todos()
    if response : 
        return response
    raise HTTPException(404, f"No TODO List found")


# to get a single task from todo based on id
@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await db.fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'No TODO item found with title : {title}') # 404 : status code for resource not found


# to post a new task in the todo list
@app.post("/api/todo", response_model=Todo)
async def add_todo(todo:Todo):
    response = await db.create_todo(todo.model_dump())
    if response : 
        return response
    raise HTTPException(400, f"Something went wrong") # 400 : status code for bad request


# to post a new task in the todo list
@app.delete("/api/todo{title}")
async def delete_todo(title:str):
    response = await db.remove_todo(title=title)
    if response : 
        return f"Successfully deleted todo : {title}"
    raise HTTPException(404, f"No TODO found with title : {title}")


# to update a task in the todo list
@app.put("/api/todo{title}", response_model=Todo)
async def update_todo(title:str, desc:str):
    response = await db.update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"No TODO found with title : {title}") # 400 : status code for bad request
      
    


