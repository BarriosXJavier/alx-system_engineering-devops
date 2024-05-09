#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List containing titles of hot articles (default is an empty list).

    Returns:
        list: List containing titles of hot articles, or None if no results are found or the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Reddit API requires a User-Agent header
    params = {"limit": 100}  # Maximum limit per request

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Check if there are more pages of results
        after = data["data"]["after"]
        if after:
            params["after"] = after
            recurse(subreddit, hot_list)  # Recursive call with updated parameters

        return hot_list
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage:
subreddit = input("Enter the name of the subreddit: ")
hot_articles = recurse(subreddit)
if hot_articles is not None:
    print("Hot articles:")
    for title in hot_articles:
        print(title)
else:
    print("No results found for the given subreddit.")
