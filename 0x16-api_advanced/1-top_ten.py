#!/usr/bin/python3
"""task_1 requests library"""
import requests


def top_ten(subreddit):
    """Get Top ten from reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"

    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
