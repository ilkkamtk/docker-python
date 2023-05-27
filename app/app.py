import os
import json
from flask import Flask
from database import Database
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Create Database instance
db = Database()


@app.route('/')
def root_route():
    return 'endpoint: /continents | /countries/:continent | /airports/:country | /airport/:icao'


@app.route('/continents')
def continents():
    db.connect()
    sql = f'''SELECT DISTINCT continent
              FROM country'''
    result = db.execute_query(sql)

    # Close the connections
    db.close()

    return json.dumps(result)


@app.route('/countries/<continent>')
def countries_by_continent(continent):
    db.connect()
    sql = f'''SELECT iso_country, name
              FROM country
              WHERE continent = %s'''
    result = db.execute_query(sql, (continent,))
    # Close the connections
    db.close()
    return json.dumps(result)


@app.route('/airports/<country>')
def airports_by_country(country):
    db.connect()
    sql = f'''SELECT ident, name, latitude_deg, longitude_deg
              FROM airport
              WHERE iso_country = %s'''
    result = db.execute_query(sql, (country,))
    # Close the connections
    db.close()
    return json.dumps(result)


@app.route('/airport/<icao>')
def airport(icao):
    db.connect()
    sql = f'''SELECT name, latitude_deg, longitude_deg
              FROM airport
              WHERE ident=%s'''
    result = db.execute_query(sql, (icao,))
    # Close the connections
    db.close()
    return json.dumps(result)


PORT = int(os.environ.get("FLASK_RUN_PORT", 8080))
if __name__ == '__main__':
    app.run(use_reloader=True, host='0.0.0.0', port=PORT)
