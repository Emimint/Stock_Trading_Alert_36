import requests
from datetime import date, timedelta
from twilio.rest import Client

# ### twilio info:
account_sid = "AC8716a929377dbc4d8c6cd7f3c18ceb2c"
auth_token = "efae5142ee99bda449734e849d3acfe8"  # /!\/!\/!\ should normally be stored as an environment variable /!\/!\/!\ !
client = Client(account_sid, auth_token)

# ### trading info:
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
my_url = "https://www.alphavantage.co/"  # /!\/!\/!\ make sur to have the ENTIRE link (here, with 'query') if you want to use parameters!
MY_API_KEY = "OZTL0DUPP624F1ES"  # /!\/!\/!\ should normally be stored as an environment variable /!\/!\/!\!

# news info:
NEWS_KEY = 'c583250647414af48cb736122a67a29c'

# daytime info:
YESTERDAY = str(date.today() - timedelta(days=1))
BEFORE_YESTERDAY = str(date.today() - timedelta(days=2))

# ## get trading info:
response = requests.get(
    f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={MY_API_KEY}')
data = response.json()
response.raise_for_status()

yesterday_stock_value = data["Time Series (Daily)"][YESTERDAY]['1. open']
bf_yesterday_stock_value = data["Time Series (Daily)"][BEFORE_YESTERDAY]['1. open']

# ## check value fluctuation:
value_change = ((float(yesterday_stock_value) / float(bf_yesterday_stock_value)) - 1) * 100

if abs(value_change) < 5:
    # ## get news info:
    news_response = requests.get(
        f'https://newsapi.org/v2/everything?q={STOCK}&from={YESTERDAY}&sortBy=popularity&apiKey={NEWS_KEY}')
    news_data = news_response.json()
    news_response.raise_for_status()

    # ## compose the SMS body:
    if value_change < 0:
        value_change_symbol = '🔻'
    else:
        value_change_symbol = '🔺'

    full_message = f'\n\n{STOCK}: {value_change_symbol}{round(value_change)}%\n'

    for i in range(0, 3):  # for first 3 articles
        headline = news_data['articles'][i]['title']
        summary = news_data['articles'][i]['description']
        full_message = full_message + f'\nHeadline: {headline}\nBrief: {summary}\n'

    message = client.messages \
        .create(
        body=full_message,
        from_='+13512474381',
        to='+15145133024'
    )
    print(message.status)
