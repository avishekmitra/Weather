'''subhelper funtions to help helper funtions'''
import os
import time
def getdatafile(filename):
    '''helper function to get the filepath from filename'''
    absolutepath = os.path.abspath(os.path.join(os.curdir, os.pardir))
    filepath = os.path.join(absolutepath, 'data', filename)
    return filepath
def getstrtime(start, end, dataformat, randomselection):
    '''helper function to genarate ISO date format'''
    stime = time.mktime(time.strptime(start, dataformat))
    etime = time.mktime(time.strptime(end, dataformat))
    ptime = stime + randomselection * (etime - stime)
    return time.strftime(dataformat, time.localtime(ptime))
def getcityname(citycode):
    '''getting cityname after passing citycode args-> cityname '''
    with open(getdatafile("UNLOCODE.txt"), encoding='cp1252') as countryfile:
        for item in countryfile:
            content = item.split('|')
            city = ''
            if content[1] == 'US' and content[len(content)-2] == str(citycode):
                city = content[3]
                return city
                break
