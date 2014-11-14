#!/usr/bin/env python
# -*- coding: utf-8 -*-
# work 3. 6
# Печать 10000 простых чисел

def counter(nomber):
	for i in xrange(2, nomber):
		if nomber%i == 0:
			return 0
			break
	return nomber


step = 0
nomb = 2
all_nomb = []

while (step < 10000):
	
	if counter(nomb) > 0:
		all_nomb.append(nomb)
		step += 1
	nomb += 1

print all_nomb
