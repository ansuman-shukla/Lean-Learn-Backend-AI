from pydantic import BaseModel
from typing import List

class FormulsSchema(BaseModel):
    id: str
    class_: str
    subject: str
    topic: str
    question: str
    options: List[str]
    answers: List[str]
    resource: List[str]
    used: bool