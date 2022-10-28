#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:05:57 2022

@author: fathimaabdulrahman
"""

def print_bin():
    a,b = list(map(int,input().split()))
    if a <= b:
        c = "10"*a+ (b-a)*'1'
    elif b <= a :
        c = '10'*b + (a-b)*'0'
    elif a == 0 or b == 0:
        c = '0'*a +'1'*b
    return c


if __name__ == "__main__":
    for i in range(int(input())): # test cases
        print(print_bin())
       
    