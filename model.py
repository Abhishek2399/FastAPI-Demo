"""

Here we will be creating the classes that will represent our data

"""



# used to map JSON type data into objects
from pydantic import BaseModel


class Todo(BaseModel):
    title : str
    description : str
