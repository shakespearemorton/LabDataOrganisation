#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:26:19 2020

@author: WilliamMorton
"""

import numpy as np
import matplotlib.pyplot as plt



def uvvis(filename,norm):
    with open(filename) as f:
        content = f.readlines()
    i = 48
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    while i <= len(content)-1:
        sample = content[i].split()
        k=0
        while True:
            x = content[i].split(',')
            try:
                float(x[0])
                break
            except:
                i+=1
                
        w=[]
        a = []
        while len(x) == 7:
            w.append(float(x[0]))
            a.append(float(x[1]))
            w.append(float(x[2]))
            a.append(float(x[3]))
            w.append(float(x[4]))
            a.append(float(x[5]))
            i+=1
            if i < len(content):
                x = content[i].split(',')
                try:
                    float(x[0])
                except:
                    x = [1]
                    
            else: 
                x = [1]
            
        w = np.array(w)
        a = np.array(a)
        if norm == 0:
            a = (a-np.min(a))/(np.max(a)-np.min(a))
            plt.ylabel('Normalised Absorbance')
        else:
            plt.ylabel('Absorbance')
        plt.xlabel('Wavelength(nm)')
        plt.scatter(w,a,label=sample[2])
        handles, labels = ax.get_legend_handles_labels()
        lgd=ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5))
        fig.savefig('uv_vis_graph.png',  bbox_inches='tight')
    return()

uvvis('final_postdmf_204062.csv',0) # first input = filename ; second input = 0 for normalised absorbance, 1 for unaltered absorbance
