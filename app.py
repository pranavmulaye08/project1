from src.project1.logger import logging
from src.project1.exception import CustomException
import sys
from src.project1.components.data_ingestion import DataIngestion
from src.project1.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_confi=DataIngestionConfig()
        data_ingestion= DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)