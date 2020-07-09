# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:24:33 2020

@author: Cory
"""

import pandas as pd
# imports data
df=pd.read_csv("andre.csv")

#only uses dates between 1977 and 1993
df=df[(df["Year"]<1994)]
df=df[ df["Year"]>1976]

#makes a histagram of the hits
df.hist("H", bins=100)