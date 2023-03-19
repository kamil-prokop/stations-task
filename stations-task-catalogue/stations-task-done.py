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

#inserting data from tables
connection = sqlite3.connect("stations-task.db")
cursor = connection.cursor()

with open('clean_measure.csv', 'r') as f:
    for row in f:
        cursor.execute("INSERT OR IGNORE INTO clean_measures (station, date, precip, tobs) VALUES (?,?,?,?)", row.split(","))
        connection.commit()

with open('clean_stations.csv', 'r') as f:
    for row in f:
        cursor.execute("INSERT OR IGNORE INTO clean_stations (station, latitude, longitude, elevation, name, country, state) VALUES (?,?,?,?,?,?,?)", row.split(","))
        connection.commit()

connection.close()

connection = sqlite3.connect("stations-task.db")
cursor = connection.cursor()
sql_select_m = f"SELECT * FROM clean_measures LIMIT 6"
sql_select_s = f"SELECT * FROM clean_stations LIMIT 6"
cursor.execute(sql_select_m)
results = cursor.fetchall()
print(results[1:6])


'''
connection = sqlite3.connect("stations-task.db")
sql_delete_m = f"DELETE FROM clean_measures"
sql_delete_s = f"DELETE FROM clean_stations"
cursor = connection.cursor()
cursor.execute(sql_delete)
connection.commit()
connection.close()
'''