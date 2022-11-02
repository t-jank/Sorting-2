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
alfa = [0.85]#[0.75,0.85,0.95,0.995]
alf = ['85%']#['75%','85%','95%','99.5%']
colors = ['crimson']#['y','m','c','r']
delta=[]

# ex_comp_q = 2*n*HarmonicNumber(n)-4*n+2*HarmonicNumber(n)
# var_ex_comp_q = 7*n^2-4*(n+1)^2*HarmonicNumber(n,2)-2*(n+1)*HarmonicNumber(n)+13*n

cc=[] # array of comparisons numbers (to calculate variance)
a=[] # array of numbers to sort
nMin=10
nMax=4000
nStep=200
nRepeat=200
sort = 'q'  # type 'q' or 'm'

for n in range(nMin, nMax, nStep):
    for rn in range(0,nRepeat):
        for i in range(0,n):
            a.append(random.randint(0,1000000000))
        if sort=='q': quicksort(a,0,len(a)-1)
        if sort=='m': mergesort(a)
        cc.append(comparison_counter)
        a.clear()
        comparison_counter = 0
    avg = statistics.mean(cc)
    for j in range(0,len(alfa)):
        delta.append(math.sqrt(statistics.variance(cc)/(1-alfa[j]))) # we wzorze: delta = a
    if sort=='m': theoretical_ex_comp = n*math.ceil(math.log(n,2))-2**(math.ceil(math.log(n,2)))+1-0.2645*n
    if sort=='q': theoretical_ex_comp = 2*n*math.log(n,math.e)
 
    plt.figure(1)
    if n==nMin:
        plt.scatter(n,theoretical_ex_comp, color='b', marker='X',label='Teoretyczna wartość oczekiwana')
        plt.scatter(n,avg, color='k', marker='o',label='Estymacja wartości oczekiwanej')
        for j in range(0,len(delta)):
            plt.scatter(n,avg+delta[j], color=colors[j], marker='.', label='Czebyszew: P(|X-EX|⩽a) ⩾ '+alf[j])#str(int(100*alfa[j]))+'%')
    else:
        plt.scatter(n,avg, color='k', marker='o')
        for j in range(0,len(delta)):
            plt.scatter(n,avg+delta[j], color=colors[j], marker='.')
        plt.scatter(n,theoretical_ex_comp, color='b', marker='X')
    for j in range(0,len(delta)):
        plt.scatter(n,avg-delta[j], color=colors[j], marker='.')
    avg=0
    cc.clear()
    delta.clear()


########### podpunkt b #################
## ustalone n, rysujemy histogram z wynikami liczby porownan
### zaznaczenie punktu n=1000 do dalszej analizy ###
n = 1000
nRepeat = 1000
color='lime'
for rn in range(0,nRepeat):
    for i in range(0,n):
        a.append(random.randint(0,1000000000))
    if sort=='q': quicksort(a,0,len(a)-1)
    if sort=='m': mergesort(a)
    cc.append(comparison_counter)
    a.clear()
    comparison_counter=0
if sort=='m': theoretical_ex_comp = n*math.ceil(math.log(n,2))-2**(math.ceil(math.log(n,2)))+1-0.2645*n
if sort=='q': theoretical_ex_comp = 2*n*math.log(n,math.e)
alfa=0.85
delta = math.sqrt(statistics.variance(cc)/(1-alfa))
avg=statistics.mean(cc)
plt.scatter(n,theoretical_ex_comp, color=color, marker='X')
plt.scatter(n,avg, color=color, marker='o')
plt.scatter(n,avg+delta, color=color, marker='.')
plt.scatter(n,avg-delta, color=color, marker='.')
odch_od_sr=[]
for o in range(0,len(cc)):
    odch_od_sr.append(abs(cc[o]-avg))
odch_od_sr.sort()
rzecz_odch = odch_od_sr[int(alfa*len(odch_od_sr))]

plt.xlim([0,nMax])
plt.ylim(bottom=0)
plt.xlabel('n - liczba elementów do posortowania')
plt.ylabel('Liczba porównań elementów')
if sort=='m': plt.title('MergeSort')
if sort=='q': plt.title("QuickSort, partycjonowanie Hoare'a")
plt.legend()
plt.show()


plt.figure(2)
plt.hist(cc)#,bins=15)
plt.axvline(x=avg,color='lime',label='Estymacja wartości oczekiwanej')
plt.axvline(x=theoretical_ex_comp, color='dimgrey',label='Teoretyczna wartość oczekiwana')
plt.axvline(x=avg+delta,color='crimson',label='Czebyszew: P(|X-EX|⩽'+str(math.ceil(delta))+') ⩾ '+str(int(100*alfa))+'%')
plt.axvline(x=avg-delta,color='crimson')
plt.axvline(x=avg+rzecz_odch,color='orangered',label='Rzeczywistośc: P(|X-EX|⩽'+str(math.ceil(rzecz_odch))+') ⩾ '+str(int(100*alfa))+'%')
plt.axvline(x=avg-rzecz_odch,color='orangered')

plt.xlabel('Liczba porównań elementów')
plt.ylabel('Liczba przypadków\n(liczba eksperymentów = '+str(nRepeat)+')')
if sort=='m': plt.title('MergeSort, n = '+str(n))
if sort=='q': plt.title("QuickSort (partycjonowanie Hoare'a), n = "+str(n))
plt.legend()
plt.show()

# orangered, crimson, yellow