#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:44:26 2022

@author: fathimaabdulrahman
"""

def cypher():
    n = int(input())
    final_numbers = list(map(int,input().split()))
    moves = []
    initial_numbers = []
    for i in range(n):
        
        wheel_move = list(input().split())
        moves.append(wheel_move)
    #print('moves',moves)
    for j in range(n):
        move = (moves)[j][1]
        ini_num = int(final_numbers[j])
        #print('current num', ini_num)
        for k in move:
            #print('k',k)
            if k == 'D' and ini_num < 9 :
                ini_num += 1
            elif k == 'D' and ini_num == 9:
                ini_num = 0
            elif k == 'U' and ini_num > 0:
                ini_num -= 1
            elif k == 'U' and ini_num == 0:
                ini_num = 9
        #print(ini_num)        
        initial_numbers.append(ini_num)
    for a in initial_numbers:
        print(a, end= " ")
        
    
if __name__ == "__main__":
    for case in range(int(input())):
        cypher()