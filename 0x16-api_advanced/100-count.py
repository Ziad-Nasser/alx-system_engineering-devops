#!/usr/bin/python3
"""requests module"""
import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    """Returns a list containing the titles of all hot articles"""
    if word_count is None:
        word_count = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/your_username)'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        return None
    
    data = response.json()['data']
    
    for post in data['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if word in word_count:
                word_count[word] += title.split().count(word)
            else:
                word_count[word] = title.split().count(word)
    
    if data['after']:
        return count_words(subreddit, word_list, data['after'], word_count)
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
        return None
