import requests
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import time
import functools

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def ttl_cache():
    def decorator(func):
        func = functools.cache(func)
        func.next_clear = time.time() + 600

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if time.time() >= func.next_clear:
                func.cache_clear()
                func.next_clear = time.time() + 600
            return func(*args, **kwargs)
        return wrapper
    return decorator

projects = ["Akshansh", "Akshansh-api"]

@app.get("/projects")
@ttl_cache()
def get_projects():
    responses = {}
    for project in projects:
        req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/{project}/main/README.md")
        print("sent request for", project)
        responses[project] = req.text
    return responses

@app.get("/projects/{project}")
@ttl_cache()
def get_project(project: str):
    if project not in projects:
        return fastapi.Response(status_code=404)
    req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/{project}/main/README.md")
    return req.text