from calendar import c
from typing import Union

from fastapi import FastAPI

app = FastAPI()




@app.get("/content/{content}")
def read_content(content: str,q: Union[str, None] = None):
    # return {"content": content, "q": q}
    print(content)
    return{"content":content,"q":q}
