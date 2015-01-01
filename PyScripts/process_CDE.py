#!/usr/bin/env python

import	numpy			as np
import	re

def	getVarDes(baseDir,CDEFileName):
	"""
	Get variable's label and description from the .CDE file

	Returns
	------
	Variables in DSSAT summary output: Dictionary
	"""
	
	sumOutCDE	= file('%s/%s'%(baseDir,CDEFileName)).readlines()
	sumOutCDEArr	= [map(str,re.split(r'\t+',sumOutCDE[i].strip())) for i in range(5,73)]
	sumOutCDEDic	= {sumOutCDEArr[i][0]:(sumOutCDEArr[i][1],sumOutCDEArr[i][2]) for i in range(np.shape(sumOutCDEArr)[0])}
	
	return sumOutCDEDic

# print	getVarDes('SUMMARYOUT.CDE').keys()
# print	getVarDes('SUMMARYOUT.CDE')['LAIX']
