# data/data_processing.py

import os
import pandas as pd
from pathlib import Path
from google.cloud import bigquery
from config import DBT_DATASET

def setup_bigquery_client():
    try:
        script_directory = Path(__file__).parent.resolve()
        credentials_path = script_directory / "airline-438510-25841398e32c.json"
        
        if not credentials_path.exists():
            raise FileNotFoundError(f"Credentials file not found at {credentials_path}")
        
        if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
            del os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(credentials_path)

        client = bigquery.Client()
        print("BigQuery Setup Complete...")
        return client
    except Exception as e:
        print(f"BigQuery Error ---> {e}")

def get_dataframe(model_name):
    """
    Fetch data from BigQuery
    """
    try:
        #client = bigquery.Client()
        #table_name = f"""{DBT_DATASET}.{model_name}"""
        #query = f"""SELECT * FROM {table_name}"""

        # Save the data to a parquet file
        #client.query(query).to_dataframe().to_parquet(f"data/local/{model_name}.parquet")
        
        # Return the saved data
        return pd.read_parquet(f"data/local/{model_name}.parquet")

    except Exception as e:
        print(f"BigQuery Error ---> {e}")

        
    except Exception as e:
        print(f"BigQuery Error ---> {e}")

def run_dbt():
    os.system("dbt run")

