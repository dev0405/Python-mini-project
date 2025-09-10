import requests

query=input("What types of news you are interested in today ? :")
API="a15bc2fca08f4f20a2c22e3e143d67de"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-07-10&sortBy=publishedAt&apiKey={API}"

r=requests.get(url)
data=r.json()
articles=data["articles"]
for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n*********************\n")