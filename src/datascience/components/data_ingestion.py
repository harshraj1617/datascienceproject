import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)

###component-data inestion

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
##downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"file already exists of path: {self.config.local_data_file}")

    ##extracting the cipfile 
    def extract_zip_file(self):
        """
        zip_file_path:str
        extracts the zip file into the data directory
        function returns none
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)