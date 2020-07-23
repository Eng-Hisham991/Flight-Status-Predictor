from flask import Flask, render_template, redirect, request
import pandas as pd
import numpy as np
import joblib
    
df= pd.read_csv('trial1.csv')
b = df['AIRLINE'].unique().tolist()
c = df['AIRLINE_P'].unique().tolist()
e = df['DEST_AIRPORT'].unique().tolist()
f = df['DEST_AIRPORT_P'].unique().tolist() 
airport = {} 
for key in b: 
    for value in c: 
        airport[key] = value 
        c.remove(value) 
        break 
dest = {}
for key in e: 
    for value in f: 
        dest[key] = value 
        f.remove(value) 
        break  
air22 = {'Mesa Airlines':'YV', 'ExpressJet':'EV','Alaska Airlines':'AS',
        'United Airlines':'UA', 'Republic Airways':'YX', 'American Airlines':'AA', 
        'Fronteir Airlines':'F9','Endeavor Air':'9E','Spirit Airlines':'NK','SkyWest Airlines':'OO',
        'Delta Airlines':'DL','JetBlue':'B6','PSA Airlines':'OH'}
airl = air22['Mesa Airlines']
u = airport[f'{airl}']
dest2 = dest['MSY']
AIRLINE = float(airport[f'{airl}'])
DEST_AIRPORT = float(dest2)









if __name__ == '__main__':
    print(AIRLINE)