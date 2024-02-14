#!/usr/bin/python3
""" returns the top ten posts """


import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and
    prints the titles of the first 10
    hot posts listed for a given subreddit """
    if type(subreddit) is not str or subreddit is None:
        print("None")
        return None
    apiurl = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/aboubakrtaibi)"
        }
    res = requests.get(apiurl, headers=header, allow_redirects=False)
    if res.status_code == 200:

        print(res)
        data = res.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for _, post in enumerate(posts[:10], start=1):
                title = post['data']['title']
                print(title)
    else:
        print("None")
        return 1
