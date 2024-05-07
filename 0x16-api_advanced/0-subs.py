#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid or if the request fails.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
    except (KeyError, ValueError):
        return 0
