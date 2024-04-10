import subprocess
import threading
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
    print("Opening Localhost in Chrome...")
    try:
        subprocess.run(["open", "-a", "Google Chrome",
                       "http://localhost:8004/docs"])
    except Exception as e:
        print(f"Could not open Chrome: {e}")


if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    start_uvicorn()
