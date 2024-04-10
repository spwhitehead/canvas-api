import subprocess
import webbrowser
import time


def start_uvicorn():
    subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8004"])


def open_browser():
    time.sleep(2)
    webbrowser.open("localhost:8000/docs")


if __name__ == "__main__":
    start_uvicorn()
    open_browser()
