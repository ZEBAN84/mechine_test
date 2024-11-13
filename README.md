Continuous Path Correction & Terrain Classification Project

 ## Project Overview

This project is designed to process and fix discontinuities in a set of latitude and longitude coordinates. These coordinates represent a path from Point A to Point B. The goal is to:

## q1-explanetion


1. **Correct Discontinuities**: Automatically identify and correct coordinates that are out of a continuous path. --- you can check it out in q1.py file the code is explaind in the file accordigly
2. **Visualize the Data**: Plot the coordinates before and after correction on a map and compare the results.--- screenshot of the html file is in images/map.png, can see the file as path_comparison_map.html
3. **Data Preprocessing**: Reading and fixing discontinuous coordinates.--- the fixed file is in latitude_longitude_cleaned.csv and images/latitude_cleaned

## query_script-explanetion


1. **Store Data in Database**: Load latitude-longitude data and terrain classifications into a PostgreSQL database.-- you can check out the proof as screenshots as images/script_exicution.png,latitude_csv_to_postger.png,terrain_csv_to_postger.png
2. **Query the Database**: Perform queries to list all the points that have a "road" terrain, excluding those labeled as "civil station".--- this spesific query is comanded in the query_script.py in line 21 to 24 this spesific functionality cant be performd because if the lack of data given in the csv file
3. **Database Interaction**: Storing the data in a PostgreSQL database and querying specific terrain data.-- the query_script.py has interacted with the postgersql the program is explaind in the file acordigly you an see the exicution screen shot as images/script_exicution.png

## Requirements

- Python 3.7 or higher
- PostgreSQL database
- Required Python libraries:
  -  `pandas`
  - `geopandas`
  - `matplotlib`
  - `psycopg2`
  - `sqlalchemy`
  - `folium`
  - `pg8000`



## database creation
CREATE TABLE latitude_logitude_details (
    id SERIAL PRIMARY KEY,
    latitude DECIMAL(6,9),
    longitude DECIMAL(6,9),
    km DECIMAL(6,9),
    terrain VARCHAR(50)
);


CREATE TABLE terrain_classification (
    id SERIAL PRIMARY KEY,
    terrain VARCHAR(50),
    distance_km DECIMAL(6,9)
    
);



given files:
     1.latitude_longitude_details (2).csv
     2.terrain_classification (2).csv
     3.Machine test junior python (2)--questions for the project
