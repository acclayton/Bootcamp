# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:46:39 2020

@author: Cory
"""


from datetime import datetime
import time

start=time.time()
runsum=0
for x in range(100000):
    runsum+=x
print(runsum)
finish=time.time()

print("it took {} seconds to run".format(finish-start))


def getTime():
    now = datetime.now().time()
    print(now)