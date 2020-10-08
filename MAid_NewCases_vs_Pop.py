# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:39:41 2020

@author: daihu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hold = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv",usecols=['population','new_cases','total_cases'])