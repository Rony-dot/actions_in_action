import requests
import os
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()
# os.getenv() will not throw error, if key not found
# but os.environ[] will throw error, if key not found [best practice]
PERSONAL_ACCESS_TOKEN = os.environ["PERSONAL_ACCESS_TOKEN"]

repo_owner = "PyGithub"
repo_name = "PyGithub"

GITHUB_BASE_URL = "https://api.github.com/repos"
REPO_URL = f"{GITHUB_BASE_URL}/{repo_owner}/{repo_name}"
COMMITS_URL = f"{GITHUB_BASE_URL}/{repo_owner}/{repo_name}/commits?page=1"
ISSUES_BASE_URL = f"{GITHUB_BASE_URL}/{repo_owner}/{repo_name}/issues"


def api_call(url):
    headers = {"Authorization": f"Bearer {PERSONAL_ACCESS_TOKEN}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(
                f"Error, status_code: {response.status_code}, url: {url}"
            )

        return response.json()
    except Exception:
        raise Exception(f"Error while api call: {url}")


def get_last_commit():
    commit_list = api_call(COMMITS_URL)
    return {
        "sha": commit_list[0].get("sha"),
        "message": commit_list[0].get("commit").get("message"),
    }


def get_issues():
    list_of_issue = []
    page_no = 0
    while True:
        page_no = page_no + 1
        issues = api_call(f"{ISSUES_BASE_URL}?page={page_no}")
        if not issues:
            break

        for indiv_issue in issues:
            list_of_issue.append(
                {
                    "title": indiv_issue.get("title"),
                    "number": indiv_issue.get("number"),
                    "state": indiv_issue.get("state"),
                }
            )
    return list_of_issue


issues = get_issues()

pprint(len(issues))
pprint("-" * 50)
pprint(issues)
pprint("-" * 50)
pprint(get_last_commit())
