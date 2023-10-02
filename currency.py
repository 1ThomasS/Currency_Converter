
def round_rate(rate):
    return round(rate, 4)
    

def reverse_rate(rate):
    if rate != 0:
        inverse_rate = 1 / rate
        return round(inverse_rate, 4)
    else:
        return 0
    
def format_output(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate):
    formatted_output = (
        f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate}. "
        f"So {amount} in {from_currency} correspond to {converted_amount} in {to_currency}. "
        f"The inverse rate was {inverse_rate}."
    )
    return formatted_output
   