#!/usr/bin/env python

import	DSSAT_LIBRARY	as	DSSAT

dims		= {}
dims['nlat']	= 1
dims['nlon']	= 1
dims['res']	= 1
dims['minlat']	= 10
dims['minlon']	= 10
dims['tStep']	= 1

baseDir		= '/Users/hexg/Dropbox/Study/Princeton_2014-2015_Fall/APC524/APC_Project_HEXG/Data'
CDEFileName	= 'SUMMARYOUT.CDE'
inFileName	= 'Summary.OUT'
outFileName	= 'Summary.nc'
varName		= 'HWAM'

out	= DSSAT.postProcess(baseDir, CDEFileName)
out.drawTimeSeries(inFileName,varName)
out.getVarValues(inFileName)[0]
out.Create_NETCDF_File(dims, inFileName, outFileName)
