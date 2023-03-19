import sqlite3

#creating 1 database with 2 tables with names of columns
connection = sqlite3.connect("stations-task.db")
cursor = connection.cursor()


#first table = clean_stations.csv
sql_clean_stations = """
CREATE TABLE IF NOT EXISTS clean_stations (
    station TEXT PRIMARY KEY,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    elevation FLOAT NOT NULL,
    name TEXT NOT NULL,
    country VARCHAR(2) NOT NULL,
    state VARCHAR(2) NOT NULL
)
"""

#second table = clean_measures.csv
sql_clean_measures = """
CREATE TABLE IF NOT EXISTS clean_measures (
    station TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    precip FLOAT NOT NULL,
    tobs INTEGER NOT NULL
)
"""

cursor.execute(sql_clean_stations)
connection.commit()

cursor.execute(sql_clean_measures)
connection.commit()
connection.close()
