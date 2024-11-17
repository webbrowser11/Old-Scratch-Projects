import requests

projectID = 100

while True:
    res = requests.get(f"https://api.scratch.mit.edu/projects/{projectID}")
    if res.ok:
        print(f"{res.json()["title"]} (https://scratch.mit.edu/projects/{projectID})")
    else:
        print(f"{projectID} is not real")
    projectID += 1
