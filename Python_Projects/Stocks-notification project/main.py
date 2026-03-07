import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

#STOCK DATA
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

percent_change = -6
if abs(percent_change) >= 5:

    NEWS_PARAMETERS = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": os.getenv("NEWS_API_KEY"),
    }

    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_data = news_response.json()
    articles = news_data.get("articles", [])[:3]
    if not articles:
        print("No articles found.")
        exit()

    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    arrow = "🔺" if percent_change > 0 else "🔻"

    for article in articles:
        message = client.messages.create(
            body=f"""{STOCK_NAME}: {arrow}{abs(percent_change)}%
Headline: {article['title']}
Brief: {article['description']}""",
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("TARGET_PHONE_NUMBER"),
        )

else:
    print("Price change less than 5% — no alert sent.")
