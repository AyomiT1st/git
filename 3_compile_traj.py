# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:17:14 2023

@author: hilario

Compiles trajectories made with gen_traj.py

"""

import os
import sys
#Repository directory: place where I put my general functions
repo_dir = 'C:\\Users\hilario\OneDrive - University of Arizona\Python\\repository'
#Tell Python to look through repo_dir as well when importing packages
if repo_dir not in sys.path:
    sys.path.append(repo_dir)
import generate_hysplit as gh

save = True
basename = 'DC3_NAM_48h'

'''Directories'''
storage_dir = f'C:\\trajectories\{basename}\\'
proj_dir = 'C:\\Users\hilario\OneDrive - University of Arizona\Python\DC3Traj\\'
inputs_dir = f'{proj_dir}inputs\\'

print('Compiling trajectories')
traj_list = os.listdir(storage_dir)
traj_all = gh.compile_traj(traj_list, storage_dir)

if save: 
    print('Exporting to csv')
    # start, end = traj_all.Launch_UTC.iloc[0].strftime('%Y%m%d'), traj_all.Launch_UTC.iloc[-1].strftime('%Y%m%d')
    # out_name = f'{basename}_{start}thru{end}'
    traj_all.to_csv(f'{inputs_dir}{basename}.csv', index = False)