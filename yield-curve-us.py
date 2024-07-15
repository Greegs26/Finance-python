import pandas as pd
import matplotlib.pyplot as plt
import requests
import io

# Step 1: Retrieve US bond yield data
url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv'
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    raise Exception(f"Failed to retrieve data: {response.status_code}")

data = response.content.decode('utf-8')

# Check if the data is not empty
if not data.strip():
    raise Exception("The retrieved data is empty")

# Step 2: Process the data
# Read the data into a pandas DataFrame using io.StringIO
df = pd.read_csv(io.StringIO(data))

# Check if the DataFrame is not empty
if df.empty:
    raise Exception("The DataFrame is empty")

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract the latest data for plotting
latest_data = df.iloc[-1]

# Extract the yield values and corresponding maturities
maturities = ['1 Mo', '2 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr', '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr']
yields = [latest_data[m] for m in maturities]

# Step 3: Plot the yield curve
plt.figure(figsize=(10, 6))
plt.plot(maturities, yields, marker='o')
plt.title(f'US Treasury Yield Curve as of {latest_data["Date"].date()}')
plt.xlabel('Maturity')
plt.ylabel('Yield (%)')
plt.grid(True)
plt.show()