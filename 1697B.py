#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:05:57 2022

@author: fathimaabdulrahman
"""

def max_free_price():
    # Input number of items and queries
    n,q = list(map(int,input().split()))
    # Input price list
    prices = list(map(int,input().split()))
    prices = prices.sort(reverse=True)
    for i in range(q):
        #Input queries with x and y
        x,y = list(map(int,input().split()))
        x_prices = prices[:x]
        free_prices = sum(x_prices[-y:])
        print(free_prices)
               

if __name__ == "__main__":
    max_free_price()
       
    