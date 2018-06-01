#%%
import os 
import numpy as np
import pandas as pd
import nita_funs as nita

#%%
os.chdir(r'C:/Users/feng/Documents/pynita')

#%%
test_data = pd.read_csv('./input/test_data.csv')

px = np.array(test_data.px)
date_vec = np.array(test_data.date_vec)
doy_vec = np.array(test_data.doy_vec)

#%%
value_limits = [0,1]
doy_limits = [[1,100],[260,365]] 
date_limits = [1995000,2010000]
bail_thresh = 1.2
noise_thresh = 1
penalty = 1
filt_dist = 5
pct = 50
max_complex = 7
min_complex = 1
compute_mask = 1
filter_opt = 'movcv'

#%%
results_dic = nita.nita_px(px, date_vec, doy_vec, 
                           value_limits, doy_limits, date_limits, bail_thresh, noise_thresh,
                           penalty, filt_dist, pct, max_complex, min_complex,
                           compute_mask, filter_opt)