#!/usr/bin/python3
"""task_0 requests library"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers from reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    elif response.status_code in [301, 302, 404]:
        return 0
    else:
        return 0
