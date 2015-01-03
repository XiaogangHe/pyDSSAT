#!/usr/bin/env python

import	numpy			as	np
import	re
import	netCDF4			as	netcdf
import	matplotlib.pyplot	as	plt

class	postProcess(object):
	def	__init__(self, baseDir, CDEFileName):
	#def	__init__(self, baseDir, fileName=None, CDEFileName=None, varName=None):
		"""
		Return a new object to post-process DSSAT output
		"""
		self._baseDir		= baseDir
		self._CDEFileName	= CDEFileName
		#self._fileName		= fileName
		#self._varName		= varName

	# Get variables and their corresponding lables and description from .CDE file
	def	getVarDes(self):
		"""
		Get variable's label and description from the .CDE file
	
		Returns
		------
		Variables in DSSAT summary output: Dictionary
		"""
	
		sumOutCDE	= file('%s/%s'%(self._baseDir, self._CDEFileName)).readlines()
		sumOutCDEArr	= [map(str,re.split(r'\t+',sumOutCDE[i].strip())) for i in range(5,73)]
		sumOutCDEDic	= {sumOutCDEArr[i][0]:(sumOutCDEArr[i][1],sumOutCDEArr[i][2]) for i in range(np.shape(sumOutCDEArr)[0])}

		return sumOutCDEDic

	# Get variables and their corresponding simulation results from the output file
	def	getVarValues(self, fileName):
		FILE	= file('%s/%s'%(self._baseDir,fileName)).readlines()
		outData	= FILE[4:]
		varId	= FILE[3]					# Read the raw variables 
		varId	= map(str,str.split(varId)[12:])		# Only get the useful variables
		bType	= map(str,str.split(FILE[4]))[5:7]		# Basic type: crop and model
		crpType	= bType[0]
		modType	= bType[1]
		nYear	= np.size(outData)
		dataArr	= np.array([map(float,str.split(outData[i])[11:]) for i in range(nYear)])   # Convert the raw data to numpy array
		dataDic	= {varId[i]:dataArr[:,i] for i in range(len(varId))} 
		sYear	= int(round(dataDic['PDAT'][0]/1000))
		eYear	= sYear+nYear
		
		return dataDic, sYear, eYear

	def	drawTimeSeries(self, fileName, varName):
		
		dataDic	= self.getVarValues(fileName)[0]
		sYear	= self.getVarValues(fileName)[1]
		eYear	= self.getVarValues(fileName)[2]
		nYear	= eYear - sYear
		Year	= np.arange(sYear,eYear)
		plt.figure()
		plt.plot(dataDic[varName],linewidth=1.5)
		plt.xlim([-1,nYear])
		plt.xticks(range(nYear)[::5],Year[::5])
		plt.xlabel('Year',fontsize=15)
		varDes	= self.getVarDes()[varName][1]
		plt.title(varDes,fontsize=20)
		plt.show()

	# Write the output to NetCDF format
	def	Create_NETCDF_File(self, dims, inFileName, outFileName):
		"""
		Creat DSSAT output to netCDF format

		Returns
		------
		DSSAT summary output: netCDF format
		"""

		dataOut	= self.getVarValues(inFileName)
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
		varsInfo= self.getVarDes()
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
		f.variables['lon'][:]		= np.linspace(minlon,minlon+res*(nlon-1),nlon)
		f.variables['lon'].units	= 'degrees_east'
		f.variables['lon'].long_name	= 'Longitude'
		f.variables['lon'].res		= res
		
		# Latitude
		f.createVariable('lat','d',('lat',))
		f.variables['lat'][:]		= np.linspace(minlat,minlat+res*(nlat-1),nlat)
		f.variables['lat'].units	= 'degrees_north'
		f.variables['lat'].long_name	= 'Latitude'
		f.variables['lat'].res		= res
			
		# Time
		times				= f.createVariable('t','d',('t',))
		f.variables['t'][:]		= t
		f.variables['t'].units		= '%s since %04d' % (tStep,tInitial)
		f.variables['t'].long_name	= 'Time'
			
		# Data
		for var in varsName:
			f.createVariable(var,'f',('t','lat','lon'))
			f.variables[var].long_name	= varsInfo[var][1]
			data				= dataDic[var]
			f.variables[var][:,0,0]		= data
			
		f.close()

		return f

