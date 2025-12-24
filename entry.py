from fastapi import APIRouter

entry_root = APIRouter()

@entry_root.get("/")
def home():
    return {"message": "Blog API running"}
