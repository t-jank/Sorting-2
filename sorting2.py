# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:43:03 2022

@author: t-jan
"""


import random

comparison_counter = 0

'''
def qsort(arr): # Lomuto
    global comparison_counter
    if len(arr) <= 1: return arr
    p = arr.pop()
    left =  [a for a in arr if a < p]
    right = [a for a in arr if a >= p]
    comparison_counter += len(arr)
    return  qsort(left) + [p] + qsort(right)
'''

def partition(arr, lo, hi): # Hoare
    global comparison_counter
    pivot = arr[int((hi+lo)/2)]
    i = lo - 1
    j = hi + 1
    while (True):
        i += 1
        comparison_counter += 1
        while (arr[i] < pivot):
            i += 1
            comparison_counter += 1
        j -= 1
        comparison_counter += 1
        while (arr[j] > pivot):
            j -= 1
            comparison_counter += 1
        if (i >= j):
            return j
        arr[i], arr[j] = arr[j], arr[i]
 

def quicksort(arr, lo, hi):
    if (lo < hi):
        pivot = partition(arr, lo, hi)
        quicksort(arr, lo, pivot)
        quicksort(arr, pivot + 1, hi)


def mergesort(arr):
    global comparison_counter
    if len(arr)==1:return arr
    s=int(len(arr)/2)
    a=mergesort(arr[:s])
    b=mergesort(arr[s:])
    a=a[::-1]
    b=b[::-1]
    i=a.pop()
    e=b.pop()
    c=[]
    for x in range(len(arr)):
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


n = 8

# ex_comp_q = 2*n*HarmonicNumber(n)-4*n+2*HarmonicNumber(n)
# ex_comp_m = n*ceil(log(2,n))-2^(ceil(log(2,n)))+1
# var_ex_comp_q = 7*n^2-4*(n+1)^2*HarmonicNumber(n,2)-2*(n+1)*HarmonicNumber(n)+13*n

a=[]
for repeat_number in range(0,10):
    for i in range(0,n):
        a.append(random.randint(0, 10))
    print(a)
    quicksort(a,0,len(a)-1)
    print(a)
 #   print(mergesort(a))
    print("Liczba porównań:", comparison_counter,"\n")
    a.clear()
    comparison_counter = 0

