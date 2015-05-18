#!/usr/bin/python

"""
Gnuplot graph generator
"""

import json
import pingparser
import numpy
from decimal import Decimal as D
import os,stat,re
from sys import argv
from Queue import Empty


def CreateBoxPlot( data, plotDict, outputFilename ):
    if plotDict is None:
        return
    with open(outputFilename+'.dat', 'w') as f:
        f.write('# x [lower whisker] [Q1] [Q2] [Q3] [upper whisker] [box width] [case]\n')
        x = 1
        for d in data:
            f.write( '%d %f %f %f %f %f %f %s\n' % (x,d[plotDict['lW']],d[plotDict['Q1']],d[plotDict['Q2']],d[plotDict['Q3']],d[plotDict['uW']],plotDict['bw'],d[plotDict['case']]) )
            x+=1
    f=os.popen('gnuplot', 'w')
    print >>f, "set terminal png transparent enhanced font \"arial,10\" fontscale 1.0 size 500,350;"
    print >>f, "set out '%s.png'" % (outputFilename)
    print >>f, "set offset graph 0.1, graph 0.1, graph 0.1, graph 0.1"
    print >>f, "set xrange[0:%d]; set yrange[0:]; set xlabel '%s'; set ylabel '%s';" % ((len(data)+1), plotDict['xlabel'], plotDict['ylabel'])
    print >>f, "plot '%s' using 1:3:2:6:5:7:xticlables(8) with candlesticks title '%s' whiskerbars, \\" % (outputFilename+'.dat', plotDict['title'])
    print >>f, "'' using 1:4:4:4:4:7 with candlesticks lt -1 notitle"
    f.flush()

    return
    
def GetDataFromFilesJson( dataFiles ):
    data=[]
    for file in dataFiles:
        with open(file, 'r') as f:
            data.append(json.loads(f.read()))
    return data

if __name__ == '__main__':
    dataFiles = argv[1:(len(argv)-2)]
    outputName = argv[len(argv)-1]
    data = GetDataFromFilesJson( dataFiles )
    plotDict_t1t0_boxplot = {'lW': 'lower_whisker_t1t0',
                             'uW': 'upper_whisker_t1t0',
                             'Q1': 'q1_t1t0',
                             'Q2': 'median_t1t0',
                             'Q3': 'q3_t1t0',
                             'bw': 0.5,
                             'case': 'number_mobiles',
                             'xlabel': 'Number of Mobiles',
                             'ylabel': 't1-t0 [ms]',
                             'title': 'Quartiles'}
    plotDict_t4t2_boxplot = {'lW': 'lower_whisker_t4t2',
                             'uW': 'upper_whisker_t4t2',
                             'Q1': 'q1_t4t2',
                             'Q2': 'median_t4t2',
                             'Q3': 'q3_t4t2',
                             'bw': 0.5,
                             'case': 'number_mobiles',
                             'xlabel': 'Number of Mobiles',
                             'ylabel': 't4-t2 [ms]',
                             'title': 'Quartiles'}}
    CreateBoxPlot(data, plotDict_t1t0_boxplot, outputName+'_t1t0')
    CreateBoxPlot(data, plotDict_t4t2_boxplot, outputName+'_t4t2')
