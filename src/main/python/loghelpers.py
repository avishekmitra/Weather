'''Capturing and logging time and logging info. of program execution'''
import logging
from helpers import getoutputdir

def loginfo(source):
    '''generic loginfo write on outputdir
       args- string message as source
    '''
    log_file = getoutputdir("weather_data.log")
    log_df = "%Y-%m-%d-%H-%M-%S"
    logging.basicConfig(level=logging.INFO, filename=log_file, filemode='w', datefmt=log_df)
    logging.info(source)
