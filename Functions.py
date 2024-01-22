# function to take input student dictionary and use to update postgres database
import pandas as pd
from sqlalchemy import create_engine

# Function to send dataframe to existing database table, arguments are data frame and table name.
def data_to_postgres(dataframe, table_name):
    
    # Initialize engine object to connect to PgAdmin postgres database
    global engine  # so 'engine' can be used in later functions
    engine = create_engine(f"postgresql://postgres:password@localhost:5432/{table_name}")

    # Export Initial Dataframe to Postgres Database, replace if already there
    dataframe.to_sql(table_name, engine, index=False, if_exists="replace")


def add_new(student_dict, table_name):
    # Bring in a dictionary, convert to dataframe, transpose columns & rows
    student_dict = pd.DataFrame.from_dict(student_dict, orient="index").T

    # Export DataFrame to PostgreSQL table "student_grades" using SQLAlchemy
    student_dict.to_sql(table_name, engine, index=False, if_exists="append")



