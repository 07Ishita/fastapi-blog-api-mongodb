from fastapi import APIRouter, HTTPException
from models.blog import BlogModel
from config.config import blogs_collection
from bson import ObjectId
import datetime

blog_root = APIRouter()

# ---------------- CREATE BLOG ----------------
@blog_root.post("/new/blog")
def create_blog(doc: BlogModel):
    blog = dict(doc)
    blog["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
    result = blogs_collection.insert_one(blog)
    blog["_id"] = str(result.inserted_id)
    return {"message": "Blog created successfully", "data": blog}


# ---------------- GET ALL BLOGS ----------------
@blog_root.get("/blogs")
def get_blogs():
    blogs = []
    for blog in blogs_collection.find():
        blog["_id"] = str(blog["_id"])
        blogs.append(blog)
    return blogs


# ---------------- GET BLOG BY ID ----------------
@blog_root.get("/blogs/{blog_id}")
def get_blog_by_id(blog_id: str):

    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID")

    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    blog["_id"] = str(blog["_id"])
    return blog


# ---------------- DELETE BLOG ----------------
@blog_root.delete("/blogs/{blog_id}")
def delete_blog(blog_id: str):

    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID")

    result = blogs_collection.delete_one({"_id": ObjectId(blog_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")

    return {"message": "Blog deleted successfully"}
