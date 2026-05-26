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
writeups = ["lorem", "ipsum"]
writeups_dict = {"lorem":1, "ipsum":2}

@app.get("/")
@ttl_cache()
def get_all(
    type: str,
    name: str | None = None,
    names: bool = False
):
    if names:
        if type == "projects":
            return projects_dict
        if type == "blogs":
            return blogs_dict
        if type == "writeups":
            return writeups_dict
    else:
        if type == "projects":
            if name == None:
                responses = {}
                for project in projects:
                    req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/{project}/main/README.md")
                    responses[project] = req.text.replace("\n","").replace("    "," ")
                return responses
            else:
                req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/{name}/main/README.md")
                return req.text.replace("\n","").replace("    "," ")
        if type == "blogs":
            if name == None:
                responses = {}
                for blog in blogs:
                    req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/blogs/main/{blog}.html")
                    responses[blog] = req.text.replace("\n","").replace("    "," ")
                return responses
            else:
                req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/blogs/main/{name}.html")
                return req.text.replace("\n","").replace("    "," ")
        if type == "writeups":
            if name == None:
                responses = {}
                for writeup in writeups:
                    req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/blogs/main/writeups/{writeup}.html")
                    responses[writeup] = req.text.replace("\n","").replace("    "," ")
                return responses
            else:
                req = requests.get(f"https://raw.githubusercontent.com/Ender-always-wins/blogs/main/writeups/{name}.html")
                return req.text.replace("\n","").replace("    "," ")