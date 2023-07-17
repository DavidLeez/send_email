import requests
from send_email import send_email

api_key = "4e7d8efb067d4180a83b0d0863b0224b"
url = "https://newsapi.org/v2/top-headlines?" \
      "sources=techcrunch&" \
      f"apiKey={api_key}&" \
      "language=en"
# make request
request = requests.get(url)

# get a dictionary with data in JSON format
content = request.json()

# access the article title and description
body = ""
# if "articles" in content:
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2 * "\n"
# for article in content["articles"][:10]:
#     body = "Subject: Today's news" \
#            + "\n" + body + f"{article['title']}\n{article['description']}\n{article['url']}\n\n"
body = "Subject: Today's news" + "\n" + body
body = body.encode("utf-8")
send_email(message=body)
