import requests
import pandas as pd

# Series IDs for benchmark bond yields
series_ids = {
    "2-year": "BD.CDN.2YR.DQ.YLD",
    "3-year": "BD.CDN.3YR.DQ.YLD",
    "5-year": "BD.CDN.5YR.DQ.YLD",
    "7-year": "BD.CDN.7YR.DQ.YLD",
    "10-year": "BD.CDN.10YR.DQ.YLD",
    "Long-term": "BD.CDN.LONG.DQ.YLD"
}

# Function to get latest observation for a series
def get_latest_yield(series_id):
    url = f"https://www.bankofcanada.ca/valet/observations/{series_id}/json"
    r = requests.get(url)
    data = r.json()

    if 'observations' not in data:
        print(f"Error for series {series_id}: {data}")
        return None, None

    observations = data['observations']
    if not observations:
        return None, None

    latest = observations[-1]
    date = latest['d']
    value = latest[series_id]['v']
    return date, float(value)

# Wrapper function to fetch all yields
def get_canadian_yields():
    yields = {}
    for label, series_id in series_ids.items():
        date, value = get_latest_yield(series_id)
        if date and value:
            yields[label] = value
    return yields