#!/usr/bin/env python3

import os
import json

from github import Github
#from get_robot_token import get_best_robot_token

if __name__ == "__main__":
    GITHUB_EVENT_PATH = os.getenv("GITHUB_EVENT_PATH", "")
    with open(GITHUB_EVENT_PATH, "r", encoding="utf-8") as event_file:
        github_event = json.load(event_file)
    commit_sha = github_event["pull_request"]["head"]["sha"]
    
    print(commit_sha);
    
    GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY", "yakov-olkhovskiy/TestPub")
    print(GITHUB_REPOSITORY);
    gh = Github(os.getenv("SOMETHING"))
    repo = gh.get_repo(GITHUB_REPOSITORY)
    commit = repo.get_commit(commit_sha)
    
    NAME = "My Check"
    commit.create_status(
            context=NAME,
            description="Created check",
            state="error",
#            target_url=url,
        )
