from src.MlProject.logger import logging
from src.MlProject.exception import CustomException
from src.MlProject.components.data_ingestion import DataIngestion
import sys
if __name__ == "__main__":
    logging.info('The execution has started')

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exxception")
        raise CustomException(e,sys)