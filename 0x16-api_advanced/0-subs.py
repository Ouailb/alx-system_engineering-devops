#!/usr/bin/python3
""" returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and
    returns the number of subscribers """
    if type(subreddit) is not str or subreddit is None:
        return 0
    apiurl = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
    res = requests.get(apiurl, headers=header, allow_redirects=False)
    if res.status_code == 404:
        return 0
    num_subscribers = res.json().get("data").get("subscribers")
    return num_subscribers
