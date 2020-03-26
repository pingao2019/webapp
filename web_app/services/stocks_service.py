# web_app/services/stocks_service.pyimport requests
import json
import os
from dotenv import load_dotenvload_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY}"

print(request_url)response = requests.get(request_url)

print(type(response)) #> <class 'requests.models.Response'>
print(response.status_code) #> 200
print(type(response.text)) #> <class 'str'>parsed_response = json.loads(response.text)

print(type(parsed_response)) #> <class 'dict'>