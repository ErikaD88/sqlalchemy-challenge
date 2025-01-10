# Import the dependencies.
from flask import Flask, jsonify
from flask_caching import Cache
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

app = Flask(__name__)

# Configure caching
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask routes with caching
@app.route("/")
@cache.cached(timeout=600)  # Cache for 10 minutes
def home():
    return (f"<center><h2>Welcome to the Hawaii Climate Analysis Local API!</h2></center>"
            f"<center><h3>Select from one of the available routes:</h3></center>"
            f"<center>/api/v1.0/precipitation</center>"
            f"<center>/api/v1.0/stations</center>"
            f"<center>/api/v1.0/tobs</center>"
            f"<center>/api/v1.0/start/end</center>"
            )

# /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
@cache.cached(timeout=300)  # Cache for 5 minutes
def precip():
    # Calculate the date one year from the last date in data set.
    previousYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= previousYear).all()

    session.close()
    
    # Dictionary with the date as the key and the precipitation (prcp) as the value
    precipitation = {date: prcp for date, prcp in results}
    
    # Convert to a json
    return jsonify(precipitation)

# /api/v1.0/stations route
@app.route("/api/v1.0/stations")
@cache.cached(timeout=300)
def stations():
    # Show a list of stations
    results = session.query(Station.station).all()
    session.close()

    stationList = list(np.ravel(results))
    
    # Convert to a json and display
    return jsonify(stationList)

# /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
@cache.cached(timeout=300)
def temperatures():
    # Calculate the date one year from the last date in data set.
    previousYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the temperatures from the most active station from the past year
    results = session.query(Measurement.tobs).\
                filter(Measurement.station == 'USC00519281').\
                filter(Measurement.date >= previousYear).all()

    session.close()

    temperatureList = list(np.ravel(results))

    # Return the list of temperatures
    return jsonify(temperatureList)

# /api/v1.0/start/end and /api/v1.0/start routes
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
@cache.cached(timeout=300)
def dataStats(start=None, end=None):
    # Select statement
    selection = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    if not end:
        startDate = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*selection).filter(Measurement.date >= startDate).all()
        session.close()
        temperatureList = list(np.ravel(results))
        return jsonify(temperatureList)
    else:
        startDate = dt.datetime.strptime(start, "%Y-%m-%d")
        endDate = dt.datetime.strptime(end, "%Y-%m-%d")
        results = session.query(*selection)\
            .filter(Measurement.date >= startDate)\
            .filter(Measurement.date <= endDate).all()
        session.close()
        temperatureList = list(np.ravel(results))
        return jsonify(temperatureList)

# App launcher
if __name__ == '__main__':
    app.run(debug=True)