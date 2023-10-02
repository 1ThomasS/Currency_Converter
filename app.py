import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_historical_rate, get_latest_rates
from currency import reverse_rate, round_rate, format_output

st.title('FX Converter')

cur_list = get_currencies_list()

if cur_list == None:
    st.error('Error!')

else:
    amount = st.number_input("Amount to be converted", min_value=0.01, step=0.01)
    from_currency = st.selectbox("From Currency", cur_list)
    to_currency = st.selectbox("To Currency", cur_list)
    
    if st.button("Get Latest Rate"):
        date, rate = get_latest_rates(from_currency, to_currency, amount)
        if date != None and rate != None:
            converted_amount = round_rate(amount * rate)
            inverse_rate = reverse_rate(rate)
            format_final = format_output(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate)
            st.success(format_final)
        else:
            st.error("Error: Unable to retrieve latest rates.")


    date = st.date_input("Select Date:", datetime.date.today())

    if st.button("Get Historical Rate"):
        rate = get_historical_rate(from_currency, to_currency, date, amount)
        if rate != None:
            converted_amount = round_rate(amount * rate)
            inverse_rate = reverse_rate(rate)
            format_final = format_output(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate)
            st.success(format_final)
        else:
            st.error("Error: Unable to retrieve historical rates.")











