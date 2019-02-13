import time
import requests
import random
import os
import rasterio
import numpy as np
from affine import Affine
from pyproj import Proj, transform
import itertools
import rasterio.features
import rasterio.warp
from datetime import datetime, timedelta


conditions = {"Sunny": {"temperature": (40, 10), "pressure": (1200, 700), "humidity": (70, 55)}, 
              "Rain": {"temperature": (25, 15), "pressure": (1200, 700), "humidity": (70, 55)}, 
              "Snow": {"temperature": (-1, -7), "pressure": (1200, 700), "humidity": (70, 55)}}

def getiatageo(latitude, longitude):
         iatageo =''
         iatageo = requests.get('http://iatageo.com/getCode/' + str(latitude) + '/' + str(longitude)).json()['IATA'] 
         return iatageo

def getlatlong(latitude, longitude):
         latlong=str(latitude) + "," + str(longitude)
         return  latlong

def getstrtime(start, end, format, randomselection):
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))
        ptime = stime + randomselection * (etime - stime)
        actualtime=time.strftime(format, time.localtime(ptime))
        return time.strftime(format, time.localtime(ptime))

def getrandomdate(start, end, randomselection):
        randodate=getstrtime(start, end, '%Y-%m-%d %H:%M:%S', randomselection)
        return randodate

def getweather():
        weather = random.choice(list(conditions))
        condition = conditions[weather]
        (tMax, tMin) = condition["temperature"]
        (pMax, pMin) = condition["pressure"]
        (hMax, hMin) = condition["humidity"]
        temp=str(round(random.uniform(tMax, tMin), 1))
        pre=str(round(random.uniform(pMax, pMin), 1))
        humid=str(round(random.uniform(hMax, hMin), 1))
        return  weather + "|" + temp + "|" +  pre +  "|"  + humid

def getdatafile(filename):
        p=os.path.abspath(os.path.join(os.curdir, os.pardir)) ## Getting file path from filename
        filepath = os.path.join(p, 'data', filename)
        return filepath

def getcurrentdate():
        now = datetime.now() ## Getting Current Date
        return now.strftime("%Y-%m-%d %H:%M:%S")

def gethistorydate(numberofdays):
        N=numberofdays #settting days for History Data 
        date_N_days_ago = datetime.now() - timedelta(days=N)
        return date_N_days_ago.strftime("%Y-%m-%d %H:%M:%S")

def getrasterdata(datafile):
    with rasterio.open(getdatafile(datafile)) as imagefile:
        imagetransform = imagefile.transform ## Image Collection
        affinetransform = imagetransform * Affine.translation(0.5, 0.5) ## Affile Translation

        coordinate1=Proj(imagefile.crs) ## Getting CRS 

        axis=imagefile.read(1)          ## Reading Axis

        cols, rows = np.meshgrid(np.arange(axis.shape[1]), np.arange(axis.shape[0])) ## Creating meshgrip for columns and rows

        rc2en = lambda r, c: (c, r) * affinetransform  ## calling lambda 
        eastings, northings = np.vectorize(rc2en, otypes=[np.float, np.float])(rows, cols) ## evaluting eastings, northings

        coordinate2=Proj(proj='latlong', datum='WGS84')
        longitude, latitude = transform(coordinate1, coordinate2, eastings, northings)
        return longitude, latitude

def getoutputdir(filename, subdir='output'):   
        tdir = os.path.join(os.getcwd(), os.pardir, subdir, filename)
        return tdir
