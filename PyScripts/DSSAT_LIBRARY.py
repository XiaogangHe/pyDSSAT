#!/usr/bin/env python

import	numpy			as	np
import	re
import	netCDF4			as	netcdf
import	matplotlib.pyplot	as plt



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

def	processOut(fileName):
	FILE	= file('%s/%s'%(baseDir,fileName)).readlines()
	outData	= FILE[4:]
	varId	= FILE[3]					# Read the raw variables 
	varId	= map(str,str.split(varId)[12:])		# Only get the useful variables
	bType	= map(str,str.split(FILE[4]))[5:7]		# Basic type: crop and model
	crpType	= bType[0]
	modType	= bType[1]
	nYear	= np.size(outData)
	dataArr	= np.array([map(float,str.split(outData[i])[11:]) for i in range(nYear)])	# Convert the raw data to numpy array
	dataDic	= {varId[i]:dataArr[:,i] for i in range(len(varId))} 
	sYear	= int(round(dataDic['PDAT'][0]/1000))
	eYear	= sYear+nYear
	Year	= np.arange(sYear,eYear)

	plt.figure()
	plt.plot(dataDic[varName],linewidth=1.5)
	plt.xlim([-1,nYear])
	plt.xticks(range(nYear)[::5],Year[::5])
	plt.xlabel('Year',fontsize=15)
	varDes	= getVarDes(baseDir,'SUMMARYOUT.CDE')[varName][1]
	plt.title(varDes,fontsize=20)
	plt.show()
	
	return dataDic, sYear, eYear

def	Create_NETCDF_File(dims, inFileName, outFileName):
	"""
	Creat DSSAT output to netCDF format

	Returns
	------
	DSSAT summary output: netCDF format
	"""

	dataOut	= processOut(inFileName)
	dataDic	= dataOut[0]
	tInitial= dataOut[1]
	nt	= dataOut[2]-tInitial
	t	= np.arange(0,nt)
	
	nlat	= dims['nlat']
	nlon	= dims['nlon']
	res	= dims['res']
	minlat	= dims['minlat']
	minlon	= dims['minlon']
	tStep	= dims['tStep']

	# Get variable names, their description and data
	varsInfo= getVarDes(baseDir,CDEFileName)
	varsName= varsInfo.keys()

	# Prepare the netCDF file
	# Create file
	f	= netcdf.Dataset(outFileName,'w')

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
		f.createVariable(var,'f',('t','lat','lon'))
		f.variables[var].long_name = varsInfo[var][1]
		data = dataDic[var]
		f.variables[var][:,0,0] = data
	
	f.close()

	return f

dims            = {}
dims['nlat']    = 1
dims['nlon']    = 1
dims['res']     = 1
dims['minlat']  = 10
dims['minlon']  = 10
dims['tStep']   = 1

baseDir         = '/Users/hexg/Dropbox/Study/Princeton_2014-2015_Fall/APC524/APC_Project_HEXG/Data'
CDEFileName     = 'SUMMARYOUT.CDE'
inFileName      = 'Summary.OUT'
outFileName     = 'Summary.nc'
varName		= 'HWAH'

Create_NETCDF_File(dims, inFileName,outFileName)
