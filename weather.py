## 1. Import required external packages ##
import urllib.request as urllib2
import numpy as np
import datetime
import sys
import math
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
import time
from math import log10,exp
## 2. Static URL and Data file location setup from http://www.bom.gov.au/catalogue/anon-ftp.shtml ftp location #
dummy_URL="ftp://ftp2.bom.gov.au/anon/gen/fwo/IDA00100.dat"
dummy_SITE="066062"
dummy_SITE_NAME ="Sydney"
## Call the ftp location to read data file from server then render and display the weather data##
class dataForecast:
 data = []
 service = ""
 prefix = "%s#%s#" % (dummy_SITE, dummy_SITE_NAME)
 error = None
## Get Location Lat/Long from City ##
def get_Location(city):
 location = geolocator.geocode(city.replace("\n", ""))
 return location
def get_Elevation(lat,lon):
 r = 6376.5 *1000
 if lat<0:
  lat=-1*lat
 if lon<0:
  lon=-1*lon
  ele=r*math.sin(lat/10000000)*math.cos(lon/10000000)
  return round(ele,1)
def get_utcTime(date,time):
 time_s = datetime.datetime.strptime(str(date)+str(time), "%Y%m%d%H%M%S")
 return time_s
def get_airPressure(temp):
 ###Calculation of Air Pressure from Temp###
 Mw=18.0160 # molecular weight of water
 Md=28.9660 # molecular weight of dry air
 R=8.31432 # gas constant
 Rd=R/Md # specific gas constant for dry air
 Rv=R/Mw # specific gas constant for vapour
 Lv=2.5# heat release for condensation of water vapour [J kg-1]
 eps=Mw/Md
 hPa=611*exp(-float(Lv)/Rv*(1/float(temp)-1/273.16))
 return str(round(hPa,1))
def get_relativeHumidity(T):
 L=2.453 * log10(6) ##Latent heat of vaporization
 Rv=461 ## Gas content
 Es=(L/Rv )*(1/273 - 1/float(T))*6.11*(-1000) ##Saturation vapor pressure
 Es_percent=round(Es*100,1)
 return Es_percent
## Main processing function ###
def process_Data(dataStream):
 cols=dataStream
 City=[]
 Date=[]
 Conditions=[]
 Temp=[]
 Pos=[]
 Airpressure=[]
 RelativeHumidity=[]
 ##################### List for Output################
 i = 0
 while i<len(cols)-1:
  City.append(cols[i].replace('\n',""))
  ##g = geocoder.google([45.15, -75.14], method='elevation')
  Pos.append(str(round(get_Location(cols[i]).latitude,2))+","+str(round(get_Location(cols[i]).longitude,2))+","+str(get_Elevation(get_Location(cols[i]).latitude,get_Location(cols[i]).longitude)))
  Date.append(str(datetime.datetime.fromtimestamp(time.mktime(time.localtime(time.mktime(get_utcTime(cols[i+2],cols[i+3]).timetuple()))))))
  Conditions.append(cols[i+7])
  Temp.append(cols[i+6])
  Airpressure.append(get_airPressure(cols[i+6]))
  RelativeHumidity.append(get_relativeHumidity(cols[i+6]))
  ##### End ####
  i += 8
  ### Storing All list into Array ###
  a=np.array([City,Pos,Date,Conditions,Temp,Airpressure,RelativeHumidity]).transpose()
  return a
## Wrapper function ##
def weather_Output():
 try:
  ftp_Request = urllib2.urlopen(dummy_URL)
  ftp_Read=ftp_Request.read().decode('utf-8')[77:]
 except OSError as err:
  print("OS error: {0}".format(err))
  exit(1)
 except ValueError:
  print("Could not decode data")
  exit(1)
 except:
  print("Unexpected error:", sys.exc_info()[0])
  exit(1)
 else :
  out=process_Data(ftp_Read.split("#"))
  return out
print(np.savetxt(sys.stdout.buffer, weather_Output(), fmt='%s', delimiter='|'))