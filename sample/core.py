
## Import Required Pakages ##
import numpy as np
from pyproj import Proj, transform
import itertools
import random
import time
import sys, getopt
import logging
from helpers import  getiatageo, getlatlong, getstrtime, getrandomdate, getweather, getdatafile, getcurrentdate, gethistorydate, getrasterdata, getoutputdir


stations = {"ONT": "Sydney", "MEL": "Melbourne", "ADL": "Adelaide", "PER": "Perth", "BRB": "Brisbane",
            "RAL": "Darwin", "HOB": "Hobart", "CAN": "Canberra", "ALB": "Albany", "BEN": "Bendigo"}

round_robin_stations = itertools.cycle(stations.keys())


def main():
        logging.basicConfig(filename=getoutputdir("weather.log"), level=logging.INFO)
        logging.info("---------------------------------------")
        logging.info("Program started at :" + getcurrentdate())

        observation = int(sys.argv[1])
        if observation < 1:
         raise ValueError('Number of observations cannot be less than 1')

        logging.warning("tif file reading started at :" + getcurrentdate())
        ##Calling raster function to get longitude and latitude
        longs, lats = getrasterdata(getdatafile('cea.tif'))

        logging.info("output file writing started  :" + getcurrentdate())
        ##Opening a data output file on output folder 
        weatherFile = open(getoutputdir("weatherdata.dat"),"w")

        r=0
        for r in range(observation):
         s_long = longs[r]
         s_lats = lats[r]
         iatageo = getiatageo(round(s_lats[r],2)+r,round(s_long[r],2)+r)
         datetime = getrandomdate(gethistorydate(100), getcurrentdate(), random.random())
         weather =  getweather()
         geo =  getlatlong(round(s_lats[r],2)+r,round(s_long[r],2)+r)
         datafile = str(iatageo) + "|" + geo + "|" + datetime + "|" + weather + "\n"
         weatherFile.write(datafile)
         r = r+1
        weatherFile.close()
        logging.info("Program End!" + getcurrentdate())
        logging.info("---------------------------------------")

if __name__ == '__main__':
        main()


