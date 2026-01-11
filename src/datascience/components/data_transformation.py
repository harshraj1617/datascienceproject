import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ##Note: ypu can add different data transformation techniques such as scaler,PCA and all
    #you can perform all kinds of EDA in ML cycle here before passsing this data to model training

    #i am only adding train_test_split cuz this data is already cleaned up and this is not an ml course :)

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info(f"train and test data splitted and saved at {self.config.root_dir}")
        logger.info(f"train data shape : {train.shape} and test data shape : {test.shape}")

        print(train.shape)
        print(test.shape)