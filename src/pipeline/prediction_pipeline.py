# We will get the prediction input from a user from a website(form)
# Then we wil call get_data_as_dataframe(self) to convert input data into a dataframe
# Next we will call predict() function.



import os
import sys
import pandas as pd
from src.logger import logging
from src.exceptions import CustomException

class PredictPipeline:

    def __init__(self):
        pass
    
    def predict(self,features):

        try:
            # Creating Preprocessor Model Path 
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')

            # ML model Path
            model_path = os.path.join('artifacts','model.pkl')

            # Preprocessor and ML Model Loading
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)
            return pred


        except Exception as e:
            logging.info("Exception occured in prediction file.")
            raise CustomException(e,sys)

    
class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
            
            self.carat=carat
            self.depth=depth
            self.table=table
            self.x=x
            self.y=y
            self.z=z
            self.cut = cut
            self.color = color
            self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys) 