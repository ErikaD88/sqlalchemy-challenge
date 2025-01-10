# sqlalchemy-challenge

This repository is designed to make a climate analysis on Honolulu, Hawaii, to help clients with trip planning and outline what they need to do during their vacation. It provides a flask-based api for analyzing historical climate data. The dataset includes temperature observations and precipitation data from various weather stations in Hawaii.

## Project Structure
- **app.py**: The Flask application that defines API routes and interacts with the SQLite database.
- **climate_analysis.ipynb**: A Jupyter Notebook for data exploration and analysis.
- **hawaii.sqlite**: The SQLite database containing the climate data.
- **hawaii_measurements.csv**: CSV file with measurement data.
- **hawaii_stations.csv**: CSV file with station information.

## API Endpoints

### Home
- **`/`**
  Displays a list of available routes in a user-friendly format.

### Precipitation Data
- **`/api/v1.0/precipitation`**
  Returns a JSON object containing precipitation data for the past year.

### Station Data
- **`/api/v1.0/stations`**
  Returns a list of all weather stations.

### Temperature Observations
- **`/api/v1.0/tobs`**
  Returns temperature observations for the most active station over the past year.

### Temperature Statistics
- **`/api/v1.0/<start>`**
  Calculates and returns TMIN, TAVG, and TMAX for all dates from the given start date (format: `YYYY-MM-DD`).

- **`/api/v1.0/<start>/<end>`**
  Calculates and returns TMIN, TAVG, and TMAX for dates between the given start and end dates (format: `YYYY-MM-DD`).

### Example API Call
```python
# Import the requests library
import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/api/v1.0/2016-01-01/2016-12-31"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Temperature statistics for the range 2016-01-01 to 2016-12-31:")
    print(f"Minimum Temperature: {data[0]}")
    print(f"Maximum Temperature: {data[1]}")
    print(f"Average Temperature: {data[2]}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

## Expected Output
Temperature statistics for the range 2016-01-01 to 2016-12-31:
- Minimum Temperature: 62.0
- Maximum Temperature: 85.0
- Average Temperature: 72.9

```
## Setup and Usage
1. Install dependencies:
   ```bash
   pip install flask sqlalchemy numpy pandas
   ```
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Access the API locally at `http://127.0.0.1:5000/`.


