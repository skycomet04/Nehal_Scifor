from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import date
import uvicorn

app=FastAPI()

class Blog(BaseModel):
    title:str
    blog_body:str

blogs={
    1:{
        'title':'Testing',
        'blog_body':'checking the working of get method'
    }
}

@app.get('/')
def home():
    return{'Blogs':blogs}

@app.get('/blog/{blog_id}')
def blog_detail(blog_id:int):
    if blog_id not in blogs:
        raise HTTPException(status_code=404,detail='Blog not found')
    return blogs[blog_id]

@app.post('/createblog/')
def create_blog(post:Blog):
    count=len(blogs)+1
    blogs[count]=post
    return blogs[count]
@app.delete('/delete_blog/{blog_id}')
def deleteblog(blog_id:int):
    if blog_id not in blogs:
         raise HTTPException(status_code=404,detail='Blog not exist.Cannot delete it')
    del blogs[blog_id]
    return{"Message":'Successfully deleted'}
