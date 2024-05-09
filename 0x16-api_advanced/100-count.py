#!/usr/bin/python3

from collections import Counter
import requests


def count_words(subreddit, word_list, counts=None):
    """
    Recursively query the Reddit API, parse the titles of all hot articles,
    and print a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count occurrences of.
        counts (Counter): Counter object to store counts of keywords (default is None).

    Returns:
        None
    """
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Reddit API requires a User-Agent header
    params = {"limit": 100}  # Maximum limit per request

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return

    try:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()  # Convert title to lowercase
            for word in word_list:
                if word.lower() in title.split():
                    counts[word.lower()] += 1

        # Check if there are more pages of results
        after = data["data"]["after"]
        if after:
            params["after"] = after
            count_words(
                subreddit, word_list, counts
            )  # Recursive call with updated parameters
        else:
            # Print the sorted count of keywords
            for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
                print(f"{word}: {count}")

    except Exception as e:
        print(f"Error: {e}")


# Example usage:
subreddit = input("Enter the name of the subreddit: ")
word_list = input("Enter the list of keywords (separated by spaces): ").split()
count_words(subreddit, word_list)
