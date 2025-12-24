from pydantic import BaseModel
from typing import List, Optional

class BlogModel(BaseModel):
    title: str
    sub_title: Optional[str] = None
    content: str
    author: str
    tags: List[str] = []
