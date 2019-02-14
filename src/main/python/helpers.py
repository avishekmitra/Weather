#!/usr/bin/env pyhton
'''helper functions to genarate the weather data'''
import time
import random
import os
from datetime import datetime, timedelta
import numpy as np
from affine import Affine
from pyproj import Proj, transform
import rasterio
import rasterio.features
import rasterio.warp
import requests
from subhelpers import getcityname,getdatafile,getstrtime


CONDITIONS = {"Sunny": {"temperature": (40, 10), "pressure": (1200, 700), "humidity": (70, 55)},
              "Rain": {"temperature": (25, 15), "pressure": (1200, 700), "humidity": (70, 55)},
              "Snow": {"temperature": (-1, -7), "pressure": (1200, 700), "humidity": (70, 55)}}

def getiatageo(latitude, longitude):
    '''helper functions to get the 3 letter city code form
        IATA website'''
    iatageo = ''
    url = 'http://iatageo.com/getCode/'
    iatageo = requests.get(url + str(latitude) + '/' + str(longitude)).json()['IATA']
    geocity = getcityname(str(iatageo))
    return geocity

def getlatlong(latitude, longitude):
    '''helper function to organise longitude, latitude output data'''
    latlong = str(latitude) + "," + str(longitude)
    return  latlong

def getrandomdate(start, end, randomselection):
    '''helper function to get a random date'''
    randodate = getstrtime(start, end, '%Y-%m-%d %H:%M:%S', randomselection)
    return randodate

def getweather():
    '''helper function to genarate the dummy weather data from dummy weather data'''
    weather = random.choice(list(CONDITIONS))
    condition = CONDITIONS[weather]
    (t_max, t_min) = condition["temperature"]
    (p_max, p_min) = condition["pressure"]
    (h_max, h_min) = condition["humidity"]
    temp = str(round(random.uniform(t_max, t_min), 1))
    pre = str(round(random.uniform(p_max, p_min), 1))
    humid = str(round(random.uniform(h_max, h_min), 1))
    return  weather + "|" + temp + "|" +  pre +  "|"  + humid

def getcurrentdate():
    '''helper function to get currentdate'''
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def gethistorydate(numberofdays):
    '''helper function to get hsitory date'''
    days_ago = datetime.now() - timedelta(days=numberofdays)
    return days_ago.strftime("%Y-%m-%d %H:%M:%S")

def getrasterdata(datafile):
    '''Get the raster longitude and latitude from .tif file'''
    with rasterio.open(getdatafile(datafile)) as imagefile:
        imagetransform = imagefile.transform
        affinetransform = imagetransform * Affine.translation(0.5, 0.5)
        coordinate1 = Proj(imagefile.crs)
        axis = imagefile.read(1)
        cols, rows = np.meshgrid(np.arange(axis.shape[1]), np.arange(axis.shape[0]))
        aftrans = lambda r, c: (c, r) * affinetransform
        eastings, northings = np.vectorize(aftrans, otypes=[np.float, np.float])(rows, cols)
        coordinate2 = Proj(proj='latlong', datum='WGS84')
        longitude, latitude = transform(coordinate1, coordinate2, eastings, northings)
        return longitude, latitude

def getoutputdir(filename, subdir='output'):
    '''helper function to get the output file directory path'''
    tdir = os.path.join(os.getcwd(), os.pardir, subdir, filename)
    return tdir
