#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:50:17 2022

@author: fathimaabdulrahman
"""

def input_row_col():
    """
    Function for getting inout for rows and columns
    """
    n, m = list(map(int,input().split()))
    return n, m    

def smallest_area():
    """
    Function for finding minimum area of a subrectangle that
    # will include the largest number
    """
    
    row , column = input_row_col()
    # Append all lists of values to a single list giving a list of lists
    a =  [] 

    max_in_rows = []    # The list of maximum values in each row of the matrix
    j_max = []   # The list of column number for the maximum value in each row
    
    # Take inputs for each row and fill the maximum values in each row and 
    # the corresponding column number for these max values
    for n in range(row): 
        vals = list(map(int,input().split()))
        a.append(vals)
    for n in range(row):
        max_in_rows.append(max(a[n]))
        j_max.append(a[n].index(max(a[n]))) 
        
    #print('max_in_rows',max_in_rows)
    #print('j_max',j_max)
    i = max_in_rows.index(max(max_in_rows))+1
    #print('i',i)
    
    j = j_max[i-1]+1
    #print('j',j)
    
    l = max(row-i+1, i)
    b = max(column-j+1,j)
    #print('l & b',l,b)
    return l*b


if __name__ == "__main__":
    for i in range(int(input())): # test cases
        print(smallest_area())
       