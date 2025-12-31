import os
import sys
import pandas as pd
import pymysql
import numpy as np
from sqlalchemy import create_engine
from src.MlProject.exception import CustomException
from src.MlProject.logger import logging
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db = os.getenv("DB_NAME")


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}/{db}"
        )
        logging.info("SQLAlchemy engine created successfully")
        df = pd.read_sql("SELECT * FROM students",engine)
        logging.info(f"Data read successfully with shape{df.shape}")

        return df
    
    except Exception as e:
        logging.eror(f"Error while reading SQL data:{e}")
        raise CustomException(e)

