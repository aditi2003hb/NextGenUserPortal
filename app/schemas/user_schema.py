from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    age: int
    permanent_string_code: str
    state: str
    country: str
