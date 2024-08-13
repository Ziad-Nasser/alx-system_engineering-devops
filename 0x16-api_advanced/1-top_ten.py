#!/usr/bin/python3
"""task_1 requests library"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    elif response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
