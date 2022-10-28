#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:37:23 2022

@author: fathimaabdulrahman
"""

def arrangeable():
    n, x = list(map(int,input().split()))
    height_array = list(map(int,input().split()))
    height_array.sort()
    check_array = []
    for i in range(n):
        if height_array[n+i] - height_array[i] < x:
            return 'NO'
    return 'YES'
        
    
if __name__ == "__main__":
    for case in range(int(input())):
        print(arrangeable())