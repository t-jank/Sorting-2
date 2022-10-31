# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:43:03 2022

@author: t-jan
"""

import random
import statistics
import matplotlib.pyplot as plt
import math

comparison_counter = 0


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


n = 1000
alfa = 0.05

# ex_comp_q = 2*n*HarmonicNumber(n)-4*n+2*HarmonicNumber(n)
# ex_comp_m = n*ceil(log(2,n))-2^(ceil(log(2,n)))+1
# var_ex_comp_q = 7*n^2-4*(n+1)^2*HarmonicNumber(n,2)-2*(n+1)*HarmonicNumber(n)+13*n

cc=[] # array of comparisons numbers (to calculate variance)
a=[] # array of numbers to sort
#avg=0
nMin=10
nMax=4000
nStep=200
nRepeat=100
for n in range(nMin, nMax, nStep):
    for rn in range(0,nRepeat):
        for i in range(0,n):
            a.append(random.randint(0,1000000000))
        quicksort(a,0,len(a)-1)
        #mergesort(a)
 #       avg += comparison_counter / nRepeat
        cc.append(comparison_counter)
        a.clear()
        comparison_counter = 0
    avg = statistics.mean(cc)
    plt.scatter(n,avg, color='k', marker='.')
    delta = math.sqrt(statistics.variance(cc)/alfa)
    plt.scatter(n,avg+delta, color='r', marker='.')
    plt.scatter(n,avg-delta, color='r', marker='.')
    avg=0
    cc.clear()
    
plt.xlim([0,nMax])
#plt.ylim([0,])
plt.xlabel('n - liczba elementow do posortowania')
plt.ylabel('En - estymacja wartosci oczekiwanej\nliczby porownan elementow')
plt.show()

#print(statistics.mean(cc))
#print(statistics.variance(cc))
