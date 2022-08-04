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
            description="0123456 10 123456 20 123456 30 123456 40 123456 50 123456 60 123456 70 123456 80 123456 90 12345 100 12345 110 12345 120 12345 130 12345 140 12345 150 12345 160 12345 170 12345 180 12345 190 12345 200",
            state="error",
#            target_url=url,
        )
