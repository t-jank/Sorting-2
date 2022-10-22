# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:43:03 2022

@author: t-jan
"""
import random

def qsort(arr):
    if len(arr) <= 1: return arr
    p = arr.pop()     
    left =  [a for a in arr if a < p]
    right = [a for a in arr if a >= p]
    return  qsort(left) + [p] + qsort(right)

def scal(n):
	if len(n)==1:return n
	s=int(len(n)/2)
	a=scal(n[:s])
	b=scal(n[s:])
	a=a[::-1]
	b=b[::-1]
	i=a.pop()
	e=b.pop()
	c=[]
	for x in range(len(n)):
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
for i in range(0,10):
    a.append(random.randint(0, 1000))


