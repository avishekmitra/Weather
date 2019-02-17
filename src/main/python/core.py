##!/usr/bin/env python
"""This script is the core module which calls helpers.py to generate weather data
"""
import sys
import random
from helpers import  getiatageo, getlatlong
from helpers import getrandomdate, getweather, getdatafile, getcurrentdate
from helpers import gethistorydate, getrasterdata, getoutputdir
from loghelpers import loginfo

# Define variables:
imagefilename = 'weather.tif' ## inputfile
outputdatafile = 'weather_data.dat' ## outputfile
historydays = 365 ## One year of history

def main():
    """This is the core module which calls helpers.py, subhelpers.py, loghelpers.py to generate weather data
    """
    loginfo("---------") ## Writing logfile
    loginfo("Data generation started") ## Writing logfile
    try:
        observation = int(sys.argv[1])  ## Argument get and check observations
        assert(observation > 1), 'Assert Error : Weather Observation must be greater than 0'
    except IndexError:
        print('1. Error : Weather observation count must be supplied on the command line')
        sys.exit(1)
    except ValueError:
        print('2. Error : Weather observation be must an positive interger')
        sys.exit(1)
    else:
        loginfo("tif file reading start") ## Writing logfile
        longs, lats = getrasterdata(getdatafile(imagefilename)) ## Calling helpers.getrasterdata
        loginfo("output file writing start")
        weather_file = open(getoutputdir(outputdatafile), "w") ##  Opening output file
        rotation_i = 0
        for rotation_i in range(observation):
            s_long = longs[rotation_i]
            s_lats = lats[rotation_i]
            iata_lats = round(s_lats[rotation_i], 2) + rotation_i
            iata_long = round(s_long[rotation_i], 2) + rotation_i
            iata_geo = getiatageo(iata_lats, iata_long) ## Getting longitude and latitude merged
            date_time = getrandomdate(gethistorydate(historydays), getcurrentdate(), random.random()) ## Get history date
            weather_data = getweather() ## Getting random weather
            geo_file = getlatlong(iata_lats, iata_long)
            elevation =  100.52 + rotation_i
            data_file = str(iata_geo) + "|" + geo_file +','+ str(elevation) + "|" + date_time + "|" + weather_data + "\n"
            weather_file.write(data_file) ## Writing final output file
            rotation_i = rotation_i + 1
        weather_file.close()
    loginfo("Program End!") ## Writing logfile
    loginfo("----------") ## Writing logfile

if __name__ == '__main__':
    main()
