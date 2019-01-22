import datetime
import sys
import time
import math
from math import log10, exp
import urllib.request as urllib2
import numpy as np
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")


URL = "ftp://ftp2.bom.gov.au/anon/gen/fwo/IDA00100.dat"
SITE = "066062"
SITE_NAME = "Sydney"

class DateForecast:
  raw_data = []
  raw_service = ""
  raw_prefix = "%s#%s#" % (SITE, SITE_NAME)
  raw_error = None
def get_location(_city):
    _location = geolocator.geocode(_city.replace("\n", ""))
    return _location
def get_elevation(_lat, _lon):
    _r = 6376.5 *1000
    if _lat < 0:
        _lat = -1*_lat
    if _lon < 0:
        _lon = -1*_lon
    _ele = _r * math.sin(_lat/10000000) * math.cos(_lon/10000000)
    return round(_ele, 1)
def get_utctime(_date, _time):
    time_s = datetime.datetime.strptime(str(_date)+str(_time), "%Y%m%d%H%M%S")
    return time_s
def get_airpressure(w_temp):
    ###Calculation of Air Prssure from Temp###
    ap_mw = 18.0160 # molecular weight of water
    ap_md = 28.9660 # molecular weight of dry air
    ap_r = 8.31432 # gas constant
    ap_rd = ap_r/ap_md # specific gas constant for dry air
    ap_rv = ap_r/ap_mw # specific gas constant for vapour
    ap_lv = 2.5 # heat release for condensation of water vapour [J kg-1]
    ap_eps = ap_mw/ap_md
    ap_hpa = 611*exp(-float(ap_lv)/ap_rv*(1/float(w_temp) - 1/273.16))
    return str(round(ap_hpa, 1))
def get_relativehumidity(w_temp):
    rh_l = 2.453 * log10(6) ##Latent heat of vaporization
    rh_rv = 461 ## Gas content
    rh_es = (rh_l/rh_rv)*(1/273 - 1/float(w_temp))*6.11*(-1000) ##Saturation vapor pressure
    es_percent = round(rh_es*100, 1)
    return es_percent

def process_wdata(data_stream):
    cols = data_stream
    w_city = []
    w_date = []
    w_conditions = []
    w_temp = []
    w_pos = []
    w_airpressure = []
    w_relativehumidity = []
    ##################### List for Output################
    i = 0
    while i < len(cols)-1:
        w_city.append(cols[i].replace('\n', ""))
        ##g = geocoder.google([45.15, -75.14], method='elevation')
        w_pos.append(str(round(get_location(cols[i]).latitude, 2))+","+str(round(get_location(cols[i]).longitude, 2))+","+str(get_elevation(get_location(cols[i]).latitude, get_location(cols[i]).longitude)))
        w_date.append(str(datetime.datetime.fromtimestamp(time.mktime(time.localtime(time.mktime(get_utctime(cols[i+2], cols[i+3]).timetuple()))))))
        w_conditions.append(cols[i+7])
        w_temp.append(cols[i+6])
        w_airpressure.append(get_airpressure(cols[i+6]))
        w_relativehumidity.append(get_relativehumidity(cols[i+6]))
        ##### End ####
        i += 8

    ### Storing All list into Array ###
    w_a = np.array([w_city, w_pos, w_date, w_conditions, w_temp, w_airpressure, w_relativehumidity]).transpose()
    return w_a

def weather_output():
    try:
        ftp_request = urllib2.urlopen(URL)
        ftp_read = ftp_request.read().decode('utf-8')[77:]
    except OSError as err:
        print("OS error: {0}".format(err))
        exit(1)
    except ValueError:
        print("Could not decode data")
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        exit(1)
    else:
        _out = process_wdata(ftp_read.split("#"))
        return _out
print(np.savetxt(sys.stdout.buffer, weather_output(), fmt='%s', delimiter='|'))
