import cfg
import pandas as pd
import numpy as np
import math

def calc_distance_bw_two_pts(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = radius * c

    return dist

def choose_census_frame_range(nlong, tol):
    # build radius of tolkm in either direction
    # Approx conversions according to https://stackoverflow.com/questions/1253499/simple-calculations-for-working-with-lat-lon-km-distance
    # Latitude: 1deg = 110.574km
    # Longitude: 1deg = 110.320*cos(latitude in radians)km
    latdelta =float(tol)/110.574
    longdelta=float(tol)/float(110.320*math.cos(math.radians(nlong)))
    return latdelta,longdelta

def find_lat_long_range(origin, dist_tol):
    r = float(dist_tol)/float(6371) #circle north south boundaries sits on the same longitude, 6371 is radius of longitudes in km, d in km
    rdeg = math.degrees(r)
    latmin = origin[0] - rdeg
    latmax = origin[0] + rdeg
    del_lon = math.degrees(math.asin(math.sin(r)/math.cos(math.radians(origin[0]))))
    lonmin = origin[1] - del_lon
    lonmax = origin[1] + del_lon
    return latmin,latmax,lonmin,lonmax

def choose_reduced_census_frame(origin,censusFrame):
    tolList=[25,50,75,100,125,250,500,1000,2000]
    tolcount=0
    i=0
    while tolcount==0:
        dist_tol = tolList[i]
        latmin,latmax,longmin,longmax = find_lat_long_range(origin,dist_tol)
        censusFrReduce = censusFrame[(censusFrame['LATITUDE']>=latmin) &
                                     (censusFrame['LATITUDE']<=latmax) &
                                     (censusFrame['LONGITUDE']<=longmax) &
                                     (censusFrame['LONGITUDE']>=longmin)==True]
        i+=1
        if censusFrReduce.shape[0]>=5:
            tolcount = 1
        if tolcount!=0:
            break
        if i>len(tolList)-1:
            censusFrReduce=censusFrame
            break
    return censusFrReduce

def calc_pop_weighted_dist_single_pt(origin,censusFrame):
    censusFrame = choose_reduced_census_frame(origin, censusFrame)
    if censusFrame.empty:
        pop_weighted_distance = 0
    else:
        censusFrame['dist'] = censusFrame.apply(lambda row: calc_distance_bw_two_pts(origin,
                                                                                     destination=(row['LATITUDE'],
                                                                                                  row['LONGITUDE'])),
                                                axis=1)
        censusFrame['PopWgt']=censusFrame.apply(lambda row: float(row['POPULATION'])/float(row['dist']),axis=1)
        if censusFrame['PopWgt'].empty:
            pop_weighted_distance = 0
        else:
            pop_weighted_distance = np.nansum(np.array(censusFrame['PopWgt']))
    return pop_weighted_distance

def calc_pop_weighted_dist_frame(address_df,pop_cent_df):
    address_df = address_df[(address_df['Lat'].isnull()==False)&(address_df['Long'].isnull()==False)==True]
    address_df['PopWgtDist'] = address_df.apply(lambda row: calc_pop_weighted_dist_single_pt((row['Lat'],row['Long']),
                                                                                             pop_cent_df),axis=1)
    return address_df
