#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Reddit API requires a User-Agent header
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except Exception as e:
        print(f"Error: {e}")
        return 0
