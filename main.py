import os

from dotenv import load_dotenv
import requests

# /api/v1/courses/:course_id/discussion_topics

load_dotenv()

access_key = os.getenv("ACCESS_TOKEN")

base_url = "https://dixietech.instructure.com/api/v1"

headers: dict[str, str] = {
    "Authorization": f"Bearer {access_key}"
}

response = requests.get(url=f"{base_url}/courses", headers=headers)
print(response.json())
