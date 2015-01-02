#!/usr/bin/env python

import	numpy	as np
import	netCDF4	as netcdf

dims	= {'nlat'	: 1,
	   'nlon'	: 1,
	   'res'	: 1,
	   'minlat'	: 10,
	   'minlon'	: 10,
	   'tInitial'	: 1970,
	   'tStep'	: 1,
	   'nt'		: 30
	  }

def	Create_NETCDF_File(dims, fileName):
	"""
	Creat DSSAT output to netCDF format

	Returns
	------
	DSSAT summary output: netCDF format
	"""

	nlat	= dims['nlat']
	nlon	= dims['nlon']
	res	= dims['res']
	minlat	= dims['minlat']
	minlon	= dims['minlon']
	t	= np.arange(0,nt)

	# Get variable names, their description and data
	varsInfo	= getVarDes(baseDir,CDEFileName)
	varsName	= varsInfo.keys()
	

	# Prepare the netCDF file
	# Create file
	f	= netcdf.Dataset(fileName,'w')

	# Define dimensions
	f.createDimension('lon',nlon)
	f.createDimension('lat',nlat)
	f.createDimension('t',len(t))
	
	# Longitude
	f.createVariable('lon','d',('lon',))
	f.variables['lon'][:] = np.linspace(minlon,minlon+res*(nlon-1),nlon)
	f.variables['lon'].units = 'degrees_east'
	f.variables['lon'].long_name = 'Longitude'
	f.variables['lon'].res = res
	
	# Latitude
	f.createVariable('lat','d',('lat',))
	f.variables['lat'][:] = np.linspace(minlat,minlat+res*(nlat-1),nlat)
	f.variables['lat'].units = 'degrees_north'
	f.variables['lat'].long_name = 'Latitude'
	f.variables['lat'].res = res
	
	# Time
	times = f.createVariable('t','d',('t',))
	f.variables['t'][:] = t
	f.variables['t'].units = '%s since %04d' % (tStep,tInitial)
	f.variables['t'].long_name = 'Time'
	
	# Data
	for var in varsName:
		f.createVariable(var,'f',('t','lat','lon'),fill_value=-9.99e+08)
		f.variables[var].long_name = varsInfo[var][1]
		fp.variables[var][0] = data

	return f

def	getVarDes(baseDir,CDEFileName):
	"""
	Get variable label and description from the .CDE file

	Returns
	------
	Variables in DSSAT summary output: Dictionary
	"""
	
	sumOutCDE	= file('%s/%s'%(baseDir,CDEFileName)).readlines()
	sumOutCDEArr	= [map(str,re.split(r'\t+',sumOutCDE[i].strip())) for i in range(5,73)]
	sumOutCDEDic	= {sumOutCDEArr[i][0]:(sumOutCDEArr[i][1],sumOutCDEArr[i][2]) for i in range(np.shape(sumOutCDEArr)[0])}
	
	return sumOutCDEDic

