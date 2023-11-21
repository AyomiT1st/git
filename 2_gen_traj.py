# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:41:59 2023

@author: hilario

Generates HYSPLIT trajectories using functions stored in generate_hysplit.py

On Anaconda Prompt:
python "C:\\Users\hilario\OneDrive - University of Arizona\Python\DC3Traj\scripts\2_gen_traj.py"

"""
import pandas as pd
import sys
#Repository directory: place where I put my general functions
repo_dir = 'C:\\Users\hilario\OneDrive - University of Arizona\Python\\repository\\'
#Tell Python to look through repo_dir as well when importing packages
if repo_dir not in sys.path:
    sys.path.append(repo_dir)
import generate_hysplit as gh

coords_file = 'dc3_coords.csv'

'''Project specific directories'''
proj_dir = 'C:\\Users\hilario\OneDrive - University of Arizona\Python\DC3Traj\\'
inputs_dir = f'{proj_dir}inputs\\'

'''HYSPLIT params'''
project = 'DC3'
runtime = -48
dataset = 'nam'
meteo_dir = f'C:\\Data\\{dataset}\\' #Drive may need to be change D:/ or C:/
vertmot = 0 #model is 0; isobaric is 1
ceiling = 15000 #10,000mAGL is too low for high altitude flights

if __name__ == "__main__": 
    print('Processing: ', dataset)

    '''Reading data'''
    coords_dir = f'{inputs_dir}{coords_file}'
    coords = pd.read_csv(coords_dir, parse_dates = ['Date_Time_UTC']).set_index('Date_Time_UTC')
    
    # coords = coords.iloc[:10] #for testing only
    
    print('Call GH')
    gh.run(coords, lat_col = 'Latitude', lon_col = 'Longitude', 
            alt_col = 'Altitude', time_col = 'Date_Time_UTC',
            runtime = runtime, project = project, dataset = dataset,
            meteo_dir = meteo_dir, ceiling = ceiling, vertmot = vertmot, skip_done = True)

#For testing
# lat_col = 'Latitude'; lon_col = 'Longitude'; 
# alt_col = 'Altitude'; time_col = 'Date_Time_UTC';
# runtime = runtime; project = project; dataset = dataset;
# meteo_dir = meteo_dir