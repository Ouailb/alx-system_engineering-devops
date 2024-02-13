#!/usr/bin/python3
"""  recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit.  """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively retrieve the titles of all hot articles for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): List to accumulate the titles of hot
    articles (default is None).
    - after (str): Token indicating the last post on the current
    page (default is None).

    Returns:
    - List of titles if posts are found, None otherwise.
    """
    if hot_list is None:
        hot_list = []
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:/1.0.0 (by /u/aboubakrtaibi)'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            after = data['data']['after'] if 'after' in data['data'] else None
            hot_list.extend(post['data']['title'] for post in posts)
            if after:
                recurse(subreddit, hot_list, after=after)
        else:
            print("Unexpected response format from Reddit API.")

    elif response.status_code == 302:
        print(f"Invalid subreddit: {subreddit}")
        return None

    else:
        print(f"Failed. Status code: {response.status_code}")

    return hot_list

