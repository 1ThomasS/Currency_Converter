from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    url = f"{BASE_URL}/currencies"

    try:
        status_code, response_content = get_url(url)

        if status_code == 200:
            currency_data = json.loads(response_content)
            currency_list = list(currency_data.keys())
            return currency_list
        else:
            return None
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def get_latest_rates(from_currency, to_currency, amount):
    url = f"{BASE_URL}/latest?amount={amount}&from={from_currency}&to={to_currency}"
    
    try:
        status_code, response_content = get_url(url)

        if status_code == 200:
            info = json.loads(response_content)
            date = info['date']
            rate = info['rates'][to_currency]
            return date, rate

        else:
            return None, None
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

def get_historical_rate(from_currency, to_currency, from_date, amount):
    url = f"{BASE_URL}/{from_date}?amount={amount}&from={from_currency}&to={to_currency}"
    
    try:
        status_code, response_content = get_url(url)
        
        if status_code == 200:
            info = json.loads(response_content)
            rate = info['rates'][to_currency]
            return rate

        else:
            return None
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
