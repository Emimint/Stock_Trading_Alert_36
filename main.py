from datetime import date, timedelta
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = "OZTL0DUPP624F1ES"

YESTERDAY = str(date.today() - timedelta(days=1))
BEFORE_YESTERDAY = str(date.today() - timedelta(days=2))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# ### Check stock prize:

response = requests.get(
    url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_API_KEY}')
data = response.json()
# print(data["Time Series (Daily)"]["2022-06-21"])

print(YESTERDAY)
print(BEFORE_YESTERDAY)
print(data["Time Series (Daily)"][YESTERDAY])
print(data["Time Series (Daily)"][BEFORE_YESTERDAY])

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
