from sqlalchemy import create_engine
import pandas as pd

# Database connection details
DB_NAME = 'geodata'
DB_USER = 'postgres'
DB_PASS = 'admin'
DB_HOST = 'localhost'
DB_PORT = 5432

# Connect to the database using SQLAlchemy with pg8000
engine = create_engine(f'postgresql+pg8000://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Define the SQL query
query = """
SELECT *
FROM latitude_longitude_details
WHERE terrain = 'road' ;
"""

# SELECT *
# FROM latitude_longitude_details
# WHERE terrain = 'road'
# AND location NOT LIKE '%civil station%';

# Execute the query and load the results into a DataFrame
try:

    df = pd.read_sql_query(query, engine)
    print("Query executed successfully. Here are the results:")
    print(df)

    # Save the results to a CSV file
    output_path = 'C:/Users/91859/Documents/vs code/mechine test/road_without_civil_station.csv'
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")
except Exception as e:
    print(f"Error executing query: {e}")
finally:
    # Dispose the engine connection
    engine.dispose()
    print("Database connection closed.")
