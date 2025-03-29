# canadian_yields.py

import requests

def get_canadian_yields():
    canadian_series_ids = {
        '1 Yr': 'V122544',
        '2 Yr': 'V122545',
        '3 Yr': 'V122546',
        '5 Yr': 'V122547',
        '7 Yr': 'V122548',
        '10 Yr': 'V122549',
        '20 Yr': 'V122550',
        '30 Yr': 'V122551'
    }

    yields = {}
    for maturity, series_id in canadian_series_ids.items():
        url = f"https://www.bankofcanada.ca/valet/observations/{series_id}/json"
        try:
            response = requests.get(url)
            data = response.json()
            latest_obs = data['observations'][-1]
            value = latest_obs[series_id]['v']
            yields[maturity] = float(value)
        except:
            yields[maturity] = None

    return {k: v for k, v in yields.items() if v is not None}