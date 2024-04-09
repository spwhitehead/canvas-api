from pydantic import BaseModel


class Course(BaseModel):
    id: int
    name: str


class Discussion(BaseModel):
    id: int
    title: str


class DiscussionEntry(BaseModel):
    message: str


class Assignments(BaseModel):
    id: int
    name: str
