import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)
@app.route("/")

def welcome():
    return(
    '''
    
    Welcome to the Climate Analysis API! <br>
    
    Available Routes: <br>
    
    /api/v1.0/precipitation <br>
    
    /api/v1.0/stations <br>
    
    /api/v1.0/tobs <br>
    
    /api/v1.0/temp/start/end (You might need to refresh this page if you receive an error initially.)
    
    ''')

# Create the precipitation route
@app.route("/api/v1.0/precipitation")

# Create the precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
       filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create the stations route
@app.route("/api/v1.0/stations")

# Create the stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create the temperature observations route
@app.route("/api/v1.0/tobs")


# Create the monthly temp function
def temp_monthly():
    temps = []
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create a summary statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")



# Create a stats function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)