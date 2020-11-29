import requests

def imp():
    res = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=3510189891224acbba5ea718b7017f9e", params={"key": "3510189891224acbba5ea718b7017f9e"})
    if res.status_code != 200:
      raise Exception("ERROR: API request unsuccessful.")
    return res.json()
