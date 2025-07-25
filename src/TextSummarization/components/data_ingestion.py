import os
import urllib.request as request

import zipfile
from src.TextSummarization.entity import DataIngestionConfig

from src.TextSummarization.logging import logger

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            ) 

            logger.info(f"file is downloaded")

        else:
            logger.info(f"file allready exist")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)              