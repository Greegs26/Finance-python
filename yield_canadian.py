import requests
import pandas as pd

# Define the series identifiers and their corresponding labels
bond_series = {
    'V39051': '2-year',
    'V39052': '3-year',
    'V39053': '5-year',
    'V39054': '7-year',
    'V39055': '10-year',
    'V39056': 'Long-term'
}

# Base URL for the Bank of Canada's Valet API
base_url = "https://www.bankofcanada.ca/valet/observations"

# Initialize a dictionary to store the latest yield data
latest_yields = {}

# Iterate over each series to fetch the latest observation
for series_id, label in bond_series.items():
    try:
        # Construct the API endpoint URL
        url = f"{base_url}/{series_id}/json?recent=1"
        # Make the GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        # Parse the JSON response
        data = response.json()
        # Extract the latest observation
        observations = data.get('observations', [])
        if observations:
            latest_observation = observations[0]
            yield_value = latest_observation.get(series_id, {}).get('v')
            if yield_value is not None:
                latest_yields[label] = float(yield_value)
            else:
                latest_yields[label] = None
        else:
            latest_yields[label] = None
    except requests.RequestException as e:
        print(f"Request error for {label} ({series_id}): {e}")
        latest_yields[label] = None
    except ValueError as e:
        print(f"Data parsing error for {label} ({series_id}): {e}")
        latest_yields[label] = None

# Convert the dictionary to a DataFrame for display
df = pd.DataFrame(list(latest_yields.items()), columns=['Term', 'Yield (%)'])
print(df)