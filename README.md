
![Surfing Image](A7F56CBE-1C00-420B-A9B5-3218505E834F.jpeg)


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
import requests
url = "http://127.0.0.1:5000/api/v1.0/precipitation"
response = requests.get(url)
print(response.json())
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

## Future Improvements
- Implement caching for frequently accessed endpoints.
- Add detailed data visualizations for API outputs.
- Optimize database queries for larger datasets.
