# yield_us.py

from fredapi import Fred
from dotenv import load_dotenv
import os

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)

def get_us_yields():
    series_ids = {
        '1 Mo': 'DGS1MO',
        '3 Mo': 'DGS3MO',
        '6 Mo': 'DGS6MO',
        '1 Yr': 'DGS1',
        '2 Yr': 'DGS2',
        '3 Yr': 'DGS3',
        '5 Yr': 'DGS5',
        '7 Yr': 'DGS7',
        '10 Yr': 'DGS10',
        '20 Yr': 'DGS20',
        '30 Yr': 'DGS30'
    }

    latest_data = {}
    for maturity, series_id in series_ids.items():
        try:
            series_data = fred.get_series(series_id)
            latest_data[maturity] = series_data.dropna().iloc[-1]
        except:
            latest_data[maturity] = None

    return {k: v for k, v in latest_data.items() if v is not None}