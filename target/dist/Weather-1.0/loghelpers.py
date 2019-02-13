import logging
from helpers import getoutputdir

def loginfo(str):
   log_file = getoutputdir("weather_data.log")
   log_df = "%Y-%m-%d-%H-%M-%S"
   log_f = '%(asctime)s %(levelname)s %(message)s'
   logging.basicConfig(level=logging.INFO, filename=log_file, filemode='w', format=log_f, datefmt=log_df)
   logging.info(str)
