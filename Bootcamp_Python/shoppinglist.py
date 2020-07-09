# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:16:16 2020

@author: Cory
"""

shoppinglist=[]

x=input("What item would you like to add to your shopping list?")

while x != "Quit":
    shoppinglist.append(x)
    x=input("What is the next item you want to add? (Type Quit to stop)")
    
for item in shoppinglist:
    print(item)