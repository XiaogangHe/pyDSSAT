#!/usr/bin/env python

import	numpy			as np
import	re

# baseDir		= '/Users/hexg/Dropbox/Study/Princeton_2014-2015_Fall/APC524/APC_Project_HEXG/Data'

def	getVarDes(baseDir,CDEFileName):
	sumOutCDE	= file('%s/%s'%(baseDir,CDEFileName)).readlines()
	sumOutCDEArr	= [map(str,re.split(r'\t+',sumOutCDE[i].strip())) for i in range(5,73)]
	sumOutCDEDic	= {sumOutCDEArr[i][0]:(sumOutCDEArr[i][1],sumOutCDEArr[i][2]) for i in range(np.shape(sumOutCDEArr)[0])}
	
	return sumOutCDEDic

# print	getVarDes('SUMMARYOUT.CDE').keys()
# print	getVarDes('SUMMARYOUT.CDE')['LAIX']
