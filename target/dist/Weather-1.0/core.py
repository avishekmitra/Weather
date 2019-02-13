## Import Required Pakages ##
import sys
import random
import logging
from helpers import  getiatageo, getlatlong
from helpers import getrandomdate, getweather, getdatafile, getcurrentdate
from helpers import gethistorydate, getrasterdata, getoutputdir
from loghelpers import loginfo


def main():
    loginfo("---------")
    loginfo("Data generation started")
    #observation = int(sys.argv[1])
    #if observation < 1:
       # raise ValueError("Number of observations cannot be less than 1")
    loginfo("tif file reading start")
    longs, lats = getrasterdata(getdatafile('cea.tif'))
    loginfo("output file writing start")
    weather_file = open(getoutputdir("weather_data.dat"), "w")
    rotation_i = 0
    for rotation_i in range(10):
        s_long = longs[rotation_i]
        s_lats = lats[rotation_i]
        iata_lats = round(s_lats[rotation_i], 2) + rotation_i
        iata_long = round(s_long[rotation_i], 2) + rotation_i
        iata_geo = getiatageo(iata_lats, iata_long)
        date_time = getrandomdate(gethistorydate(100), getcurrentdate(), random.random())
        weather_data = getweather()
        geo_file = getlatlong(iata_lats, iata_long)
        data_file = str(iata_geo) + "|" + geo_file + "|" + date_time + "|" + weather_data + "\n"
        weather_file.write(data_file)
        rotation_i = rotation_i + 1
    weather_file.close()
    loginfo("Program End!")
    loginfo("----------")

if __name__ == '__main__':
    main()
