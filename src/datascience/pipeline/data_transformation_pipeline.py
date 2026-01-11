from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path


STAGE_NAME = "Data_Transformation_Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]##this tells wheather we c=get true or false 
            if status=='True':
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            
            else:
                raise Exception("Data Validation failed. Data Transformation cannot proceed.")
            
        except Exception as e:
            print(e)

"""We also check that if the data validation is validated before proceeding towards the data tranfortmation part if not then we dont do data transformation"""