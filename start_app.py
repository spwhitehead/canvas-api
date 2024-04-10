import os
import subprocess
import sys
import webbrowser
import time


def start_uvicorn():
    uvicorn_process = subprocess.Popen(
        ["uvicorn", "main:app", "--reload", "--port", "8004"])
    try:
        uvicorn_process.wait()
    except KeyboardInterrupt:
        print("\n Stopping Uvicorn server...")
        uvicorn_process.terminate()


def open_browser():
    time.sleep(2)
    webbrowser.open("localhost:8000/docs")


if __name__ == "__main__":
    start_uvicorn()
    open_browser()
