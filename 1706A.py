#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:57:27 2022

@author: fathimaabdulrahman
"""

def lex_smallest():
    n, m = list(map(int,input().split()))
    array = list(map(int,input().split()))
    string = ['B']*m
    print('m',m)
    for i in array:
        print('i',i)
        ind = m+1-i
        print('index with m+1-i',ind)
        if i <= ind and string[i-1] == "B":
            string[i-1] ="A"
        elif i <= ind and string[i-1] == "A":
            string[ind-1] = 'A'
        if ind < i and string[ind-1]=='B':
            string[ind-1] = "A"
        elif ind < i and string[ind-1]=='A':
            string[i-1] = 'A'
    fin_string = "".join(string)
    return(fin_string)
        
if __name__ == "__main__":
    for case in range(int(input())):
        print(lex_smallest())