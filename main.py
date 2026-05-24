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
projects_dict = {"Akshansh":1, "Akshansh-api":2}
blogs = ["lorem", "ipsum"]
blogs_dict = {"lorem":1,"ipsum":2}

@app.get("/projects")
@ttl_cache()
def get_projects():
    responses = {}
    for project in projects:
        req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/{project}/main/README.md")
        responses[project] = req.text.replace("\n","").replace("    "," ")
    return responses

@app.get("/projects/{project}")
@ttl_cache()
def get_project(project: str):
    if project not in projects:
        return fastapi.Response(status_code=404)
    req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/{project}/main/README.md")
    return req.text.replace("\n","").replace("    "," ")

@app.get("/names")
@ttl_cache()
def get_names():
    return projects_dict

@app.get("/blogs")
@ttl_cache()
def get_blogs():
    responses = {}
    for blog in blogs:
        req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/blogs/main/{blog}.html")
        responses[blog] = req.text.replace("\n","").replace("    "," ")
    return responses

@app.get("/blogs/{blog}")
@ttl_cache()
def get_blog():
    if blog not in blogs:
        return fastapi.Response(status_code=404)
    req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/blogs/main/{blog}.html")
    return req.text.replace("\n","").replace("    "," ")

@app.get("/blog-names")
@ttl_cache()
def get_blog_names():
    return blogs_dict