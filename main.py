import os

from dotenv import load_dotenv
import requests
from fastapi import FastAPI

from models import Course

# /api/v1/courses/:course_id/discussion_topics

load_dotenv()

app = FastAPI()

access_key = os.getenv("ACCESS_TOKEN")

base_url = "https://dixietech.instructure.com/api/v1"

headers: dict[str, str] = {
    "Authorization": f"Bearer {access_key}"
}


@app.get("/courses")
async def get_courses() -> Course:
    response = requests.get(url=f"{base_url}/courses", headers=headers)
    r_json = response.json()

    course = Course(id=r_json[0]["id"], name=r_json[0]["name"])
    return course
