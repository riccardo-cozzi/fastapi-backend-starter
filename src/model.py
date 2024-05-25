from pydantic import BaseModel
from typing import Optional

class EmailModel(BaseModel):
    to: str
    subject: str
    body: str

