import os

from dotenv import load_dotenv
import requests
from fastapi import FastAPI

from models import Course
from models import Discussion
from models import DiscussionEntry

# /api/v1/courses/:course_id/discussion_topics

load_dotenv()

app = FastAPI()

access_key = os.getenv("ACCESS_TOKEN")

base_url = "https://dixietech.instructure.com/api/v1"

headers: dict[str, str] = {
    "Authorization": f"Bearer {access_key}"
}


@app.get("/courses")
async def get_courses() -> list[Course]:
    response = requests.get(url=f"{base_url}/courses", headers=headers)
    r_json = response.json()

    courses: list[Course] = []
    for course_json in r_json:
        course = Course(id=course_json["id"], name=course_json["name"])
        courses.append(course)

    return courses


@app.get("/discussions")
async def get_discussions(course_id: int) -> list:
    response = requests.get(
        url=f"{base_url}/courses/{course_id}/discussion_topics", headers=headers)
    r_json = response.json()

    discussions: list[Discussion] = []
    for discussion_json in r_json:
        discussion = Discussion(
            id=discussion_json["id"], title=discussion_json["title"])
        discussions.append(discussion)

    return discussions


@app.post("/discussions/entries")
async def create_discussion_entry(course_id: int, topic_id: int, body: DiscussionEntry):
    response = requests.post(url=f"{base_url}/courses/{course_id}/discussion_topics//{topic_id}/entries", headers=headers, data=body.model_dump())
    r_json = response.json()
    return
