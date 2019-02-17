'''Capturing and logging time and logging info. of program execution'''
import logging
from helpers import getoutputdir

def loginfo(source):
    '''generic loginfo write on outputdir
       args- string message as source
    '''
    log_file = getoutputdir("weather_data.log")
    frmt = '%(asctime)s %(message)s'
    logging.basicConfig(level=logging.INFO, format=frmt, filename=log_file, filemode='w')
    logging.info(source)

