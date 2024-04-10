import os

from dotenv import load_dotenv
import requests

from typing import List
from fastapi import FastAPI, Query

from models import Course
from models import Discussion
from models import DiscussionEntry
from models import Assignments

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
    response = requests.post(url=f"{base_url}/courses/{course_id}/discussion_topics//{
                             topic_id}/entries", headers=headers, data=body.model_dump())
    r_json = response.json()
    return


@app.get("/courses/{course_id}/assignments/")
async def get_assignments(course_id: int, page: int = Query(1, ge=1), per_page: int = Query(10, ge=1)) -> list[Assignments]:
    url = f"{base_url}/courses/{course_id}/assignments"
    params = {"page": page, "per_page": per_page}

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()

    assignments: List[Assignments] = []
    for assignment_json in r_json:
        assignment = Assignments(
            id=assignment_json["id"], name=assignment_json["name"])
        assignments.append(assignment)

    return assignments


@app.post("/courses/{course_id}/assignments/{assignment_id}/submit")
async def submit_assignment(course_id: int, assignment_id: int, body: Assignments):
    response = requests.post(url=f"{base_url}/courses/{course_id}/assignments/{
                             assignment_id}/submit", headers=headers, data=body.model_dump())
    r_json = response.json()
    return
