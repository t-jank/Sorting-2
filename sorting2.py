# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:43:03 2022

@author: t-jan
"""


import random

comparison_counter = 0

def qsort(arr):
    global comparison_counter
    if len(arr) <= 1: return arr
    p = arr.pop()
    left =  [a for a in arr if a < p]
    right = [a for a in arr if a >= p]
    comparison_counter += len(arr)
    return  qsort(left) + [p] + qsort(right)

def mergesort(n):
    global comparison_counter
    if len(n)==1:return n
    s=int(len(n)/2)
    a=mergesort(n[:s])
    b=mergesort(n[s:])
    a=a[::-1]
    b=b[::-1]
    i=a.pop()
    e=b.pop()
    c=[]
    for x in range(len(n)):
        comparison_counter+=1
        if(i<e):
            c.append(i)
            if not len(a)==0:
                i=a.pop()
            else:
                c.append(e)
                for q in b:
                    c.append(q)
                break    
        else:
            c.append(e)
            if not len(b)==0:
                e=b.pop()
            else:
                c.append(i)
                for q in a:
                    c.append(q)
                break
            
    return c



a=[]
for repeat_number in range(0,10):
    for i in range(0,10):
        a.append(random.randint(0, 100))
    print (a)
    print(mergesort(a))
    print("Liczba porównań:", comparison_counter,"\n")
    a.clear()
    comparison_counter = 0
