import requests

api_key = "4e7d8efb067d4180a83b0d0863b0224b"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-13&sortBy=publishedAt&apiKey=" \
      "4e7d8efb067d4180a83b0d0863b0224b"
# make request
request = requests.get(url)

# get a dictionary with data in JSON format
content = request.json()

# access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

# print(content["articles"])
