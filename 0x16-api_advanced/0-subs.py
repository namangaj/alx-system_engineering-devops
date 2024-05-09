import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        if subscribers > 0:
            return "existing subreddit"
        else:
            return "nonexisting subreddit"
    else:
        return "nonexisting subreddit"

# Example usage:
subreddit = "programming"
result = number_of_subscribers(subreddit)
print(f"Output: {result}")
