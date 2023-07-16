import requests
from send_email import send_email

api_key = "4e7d8efb067d4180a83b0d0863b0224b"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-16&sortBy=publishedAt&apiKey=" \
      "4e7d8efb067d4180a83b0d0863b0224b"
# make request
request = requests.get(url)

# get a dictionary with data in JSON format
content = request.json()

# access the article title and description
body = ""
for article in content["articles"]:
    # good solution
    body = body + f"{article['title']}\n{article['description']}\n\n"

    # original
    # if article["title"] is not None:
    # body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
