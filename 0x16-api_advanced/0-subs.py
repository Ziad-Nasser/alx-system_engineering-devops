#!/usr/bin/python3
"""task zero."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers on subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code == 404:
        return 0
    result = result.json().get("data")
    return result.get("subscribers")
