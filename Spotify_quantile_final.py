#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request
import urllib, urllib.parse
import json
from datetime import datetime, timedelta
import os
import urllib.parse
import csv
import unicodedata
import io
import time
import numpy as np 
# output results of multiple statements in one cell
from IPython.core.interactiveshell import InteractiveShell

# load libraries
from multiprocessing import freeze_support
from multiprocessing import Pool
from functools import partial
import threading
import math
import pandas as pd
import numpy as np
from random import randint
from time import sleep
import datetime, xlrd
import spotipy
import spotipy.util as util
import pandas as pd
import spotipy.oauth2 as oauth2
import time
import csv
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
import datetime, xlrd
from numpy.random import randn
from sklearn.preprocessing import QuantileTransformer
from matplotlib import pyplot
from sklearn import preprocessing
import matplotlib.pyplot as plt

danceability = []
energy = []
loudness = []
speechiness = []
instrumentalness = []
liveness = []
tempo = []
duration_ms = []
file_path = 'E://University//JKU_Master//Project_and_Thesis//docs_to_upload//24_2//Lastfm_WithSpotify1.csv'

def unique(list1): 
    x = np.array(list1) 
    return np.unique(x) 

def quantile_trans(data,n_quantiles):
    quantile_matrix = [[0 for x in range(2)] for y in range(n_quantiles)] 
    data = sorted(data)
    N = len(data)
    for i in range(0,n_quantiles-1):
        q = (N+1)*(i+1)/n_quantiles
        quantile_matrix[i][0] = i+1
        quantile_matrix[i][1] = data[int(q-1)] 
    
    quantile_matrix[n_quantiles-1][0] = n_quantiles
    quantile_matrix[n_quantiles-1][1] = data[int(N-1)] 
        
    return quantile_matrix
    
def fill_data(feature_martrix, quantiles_matrix):
    feature_new_martrix = []
    for fea in feature_martrix:
        if fea <= quantiles_matrix[0][1]:
            feature_new_martrix.append(quantiles_matrix[0][0])
        else:
            for i in range(len(quantiles_matrix)-1):
                if quantiles_matrix[i][1] < fea <= quantiles_matrix[i+1][1]:
                    feature_new_martrix.append(quantiles_matrix[i+1][0])
                    break;
                    
    return feature_new_martrix

def Spotify_quantile_danceability():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            danceability.append(row[6])
        i+=1
    return danceability


def Spotify_quantile_energy():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            energy.append(row[5])
        i+=1
    return energy

def Spotify_quantile_loudness():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            loudness.append(row[6])
        i+=1
    return loudness

def Spotify_quantile_speechiness():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            speechiness.append(row[7])
        i+=1
    return speechiness

def Spotify_quantile_instrumentalness():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            instrumentalness.append(row[8])
        i+=1
    return instrumentalness

def Spotify_quantile_liveness():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            liveness.append(row[9])
        i+=1
    return liveness

def Spotify_quantile_tempo():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            tempo.append(row[10])
        i+=1
    return tempo

def Spotify_quantile_duration_ms():
    ifile  = open(file_path, "r")
    read = csv.reader(ifile)
    i=0
    for row in read :
        if i >0:
            duration_ms.append(row[11])
        i+=1
    return duration_ms

def Spotify_quantiled():
    file_path = 'E://University//JKU_Master//Project_and_Thesis//docs_to_upload//24_2//Spotify_quantiled1.csv'
    tracks_data = open(file_path, '+a' , newline='', encoding='utf-8')
    csvwriter = csv.writer(tracks_data)

    danceability = Spotify_quantile_danceability()
    danceability_quantiles=quantile_trans(danceability,100)    
    danceability_after_quantiles = fill_data(danceability, danceability_quantiles)

    #pyplot.cla()
    #pyplot.clf()
    #plt.bar(danceability_after_quantiles,danceability,align='center')
    #plt.ylabel('danceability')
    #plt.xlabel('quantile')
    for i in range(len(danceability)):
        plt.hlines(danceability[i],0,danceability_after_quantiles[i])
    #plt.show()
    
    energy = Spotify_quantile_energy()
    energy_quantiles=quantile_trans(energy,100)    
    energy_after_quantiles = fill_data(energy, energy_quantiles)

    loudness = Spotify_quantile_loudness()
    loudness_quantiles=quantile_trans(loudness,100)    
    loudness_after_quantiles = fill_data(loudness, loudness_quantiles)        

    speechiness = Spotify_quantile_speechiness()
    speechiness_quantiles=quantile_trans(speechiness,100)    
    speechiness_after_quantiles = fill_data(speechiness, speechiness_quantiles)

    instrumentalness = Spotify_quantile_instrumentalness()
    instrumentalness_quantiles=quantile_trans(instrumentalness,100)    
    instrumentalness_after_quantiles = fill_data(instrumentalness, instrumentalness_quantiles)        

    liveness = Spotify_quantile_liveness()
    liveness_quantiles=quantile_trans(liveness,100)    
    liveness_after_quantiles = fill_data(liveness, liveness_quantiles)

    tempo = Spotify_quantile_tempo()
    tempo_quantiles=quantile_trans(tempo,100)    
    tempo_after_quantiles = fill_data(tempo, tempo_quantiles)
        
    duration_ms = Spotify_quantile_duration_ms()
    duration_ms_quantiles=quantile_trans(duration_ms,100)    
    duration_ms_after_quantiles = fill_data(duration_ms, duration_ms_quantiles)
        
    f = open(file_path, "w")
    f.write("{},{},{},{},{},{},{},{}\n".format("danceability","energy","loudness","speechiness","instrumentalness","liveness","tempo","duration_ms"))
    for x in zip(danceability_after_quantiles,energy_after_quantiles
                 ,loudness_after_quantiles,speechiness_after_quantiles
                 ,liveness_after_quantiles,liveness_after_quantiles,
                 tempo_after_quantiles,duration_ms_after_quantiles):
        f.write("{},{},{},{},{},{},{},{}\n".format(x[0], x[1],x[2], x[3],x[4], x[5],x[6], x[7]))
    f.close()
    return 0


# In[ ]:


Spotify_quantiled()


# In[ ]:




