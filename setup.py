import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Database connection information
host = "sql5.freesqldatabase.com"
port = "3306"
user = "sql5736933"
password = "njn8cESVbV"
database = "sql5736933"

# Create a connection string
connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Load the CSV file into a DataFrame
df = pd.read_csv('Data/Country_People.csv')

# Import the DataFrame into the MySQL database
# Replace 'your_table_name' with the name of your table
df.to_sql('Country_People', con=engine, if_exists='append', index=False)

print("Data imported successfully!")
