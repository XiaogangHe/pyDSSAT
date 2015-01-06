#!/usr/bin/env python
import	numpy			as	np
import	re
import	netCDF4			as	netcdf
import	matplotlib.pyplot	as	plt
import	sys, os, glob, gc, csv
from	pylab			import	*
import	datetime		as	dt
import	example

gc.collect()

class Model(object):
    def __init__(self, rnmode = 'S', fileb = '', filectl = '', filex = '', fileio = '', trnarg = '', output_file_name = '/Summary.OUT'):
        self._rnmode = rnmode
        self._fileb = fileb
        self._filectl = filectl
        self._filex = filex
        self._fileio = fileio
        self._trnarg = trnarg
        self._output_file_name = output_file_name
        self._work_path = os.getcwd()
        self._crop_type = ''
        self._soil_type = ''
    # self._modelarg = modelarg
    def run(self):
        # Run DSSAT Model
        
        self._rnmode.upper()
        
        # Select mode the DSSAT model use
        if self._rnmode == 'A':
            assert self._fileb.strip()
            assert self._filectl.strip()
        elif self._rnmode == 'C' or self._rnmode == 'G':
            assert self._filex.strip()
            assert self._trnarg.strip()
            assert self._filectl.strip()
            assert self._trnarg.strip()
        elif self._rnmode == 'B' or 'N' or 'Q' or 'S' or 'F' or 'T' or 'E' or 'L':
            assert self._fileb.strip()
            assert self._filectl.strip()
        elif self._rnmode == 'D':
            assert self._fileio.strip()
        else: raise Exception("You should input right DSSAT mode! Choose one of the following characters: A B C D E F G L N Q S T")
        
        # Call the Wrapped fortran code
        example.csm(self._rnmode, self._fileb, self._filectl, self._filex, self._fileio, self._trnarg)
        
        # Check whether we have get the output file
        file_path = self._work_path + self._output_file_name
        assert os.path.exists(file_path)


class File(object):
	def __init__(self, crop='Maize', weather='DTCM', st_yr=1948, ed_yr=2012, plant_month=6, plant_date=10, mode='S'):

		# initialization
		self.crop = crop
		self.weather = weather
		self.st_yr = st_yr
		self.ed_yr = ed_yr
		self.plant_month = plant_month
		self.plant_date = plant_date
		self.mode = mode

		self.Batch()
		self.Control()

	def Batch(self):
		batchfile = open("run.v45", "w")
		if self.mode == "S":
			batchfile.write("$BATCH(SPATIAL)\n!\n")
			batchfile.write(
				"@FILEX                                                                                        TRTNO     RP     SQ     OP     CO\n")
			batchfile.write(
				"%s%s.GSX                                                                                     %d       %d      %d      %d      %d" % (
					self.weather, str(self.st_yr), 1, 1, 0, 0, 0))

		elif self.mode == "N":
			batchfile.write("$BATCH(SEASONAL)\n!\n")
			batchfile.write(
				"@FILEX                                                                                        TRTNO     RP     SQ     OP     CO\n")
			batchfile.write(
				"%s%s.SNX                                                                                      %d       %d      %d      %d      %d" % (
					self.weather, str(self.st_yr), 1, 1, 0, 0, 0))

		elif self.mode == "B":
			batchfile.write("$BATCH(BATCH)\n!\n")
			batchfile.write(
				"@FILEX                                                                                        TRTNO     RP     SQ     OP     CO\n")
			batchfile.write(
				"%s%s.BTX                                                                                     %d       %d      %d      %d      %d" % (
					self.weather, str(self.st_yr), 1, 1, 0, 0, 0))

		elif self.mode == "D":
			batchfile.write("$BATCH(DEBUG)\n!\n")
			batchfile.write(
				"@FILEX                                                                                        TRTNO     RP     SQ     OP     CO\n")
			batchfile.write(
				"%s%s.DGX                                                                                     %d       %d      %d      %d      %d" % (
					self.weather, str(self.st_yr), 1, 1, 0, 0, 0))

		else:
			print "Missing Running Mode!\n"
			exit()

		batchfile.close()
		return

	def Control(self):
		if self.mode == "S":
			file = open("%s%s.GSX" % (self.weather, str(self.st_yr)), "w")
		elif self.mode == "N":
			file = open("%s%s.SNX" % (self.weather, str(self.st_yr)), "w")
		elif self.mode == "B":
			file = open("%s%s.BTX" % (self.weather, str(self.st_yr)), "w")
		elif self.mode == "D":
			file = open("%s%s.DGX" % (self.weather, str(self.st_yr)), "w")
		# Header
		else:
			print "Missing Running Mode!\n"
			exit()
		file.write("*EXP.DETAILS: %s%s\n" % (self.weather, str(self.st_yr)))
		file.write("\n*GENERAL\n@PEOPLE\nICASA\n@ADDRESS\nICASA\n@SITE\nChiang Mai, Thailand\n")

		# Location information
		file.write("@ PAREA  PRNO  PLEN  PLDR  PLSP  PLAY HAREA  HRNO  HLEN  HARM.........\n")
		file.write("    %d   %d   %d   %d   %d   %d   %d   %d   %d   %d\n" % (
			-99, -99, -99, -99, -99, -99, -99, -99, -99, -99))

		# Treatment
		file.write("\n*TREATMENTS                        -------------FACTOR LEVELS------------\n")
		file.write("@N R O C TNAME.................... CU FL SA IC MP MI MF MR MC MT ME MH SM\n")
		# trnum = 3
		# treatment[:,0] = range(trnum)+1
		treatment = np.zeros((1, 4))
		treatment[0, 0:2] = [1, 1]
		factorlev = np.zeros((1, 13))
		loc = [0, 1, 4, 12]
		for i in loc:
			factorlev[0, i] = 1
		file.write("%2d %d %d %d %s                    %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  %d\n" % (
			treatment[0, 0], treatment[0, 1], treatment[0, 2], treatment[0, 3], "SPATIAL", factorlev[0, 0],
			factorlev[0, 1],
			factorlev[0, 2], factorlev[0, 3], factorlev[0, 4], factorlev[0, 5], factorlev[0, 6], factorlev[0, 7],
			factorlev[0, 8], factorlev[0, 9], factorlev[0, 10], factorlev[0, 11], factorlev[0, 12]))

		# Cultivar
		file.write("\n*CULTIVARS\n")
		file.write("@C CR INGENO CNAME\n")
		if self.crop == "Maize":
			file.write("%2s %s %s %s %d\n" % (1, "MZ", "IB0012", "PIO", 3382))
		else:
			print "ERROR cultivar"

		# Fields for weather
		file.write("\n*FIELDS\n")
		file.write("@L ID_FIELD WSTA....  FLSA  FLOB  FLDT  FLDD  FLDS  FLST SLTX  SLDP  ID_SOIL    FLNAME\n")
		if self.weather == "DTCM":
			file.write("%2s %8s %4s       %d     %d %s     %d     %d %s %d    %d  %s %d\n" % (
				1, "DTCM0001", "DTCM", -99, 0, "DR000", 0, 0, "00000", -99, -99, "IB00000010", -99))
		else:
			print "ERROR field"
		file.write("@L ...........XCRD ...........YCRD .....ELEV .............AREA .SLEN .FLWR .SLAS FLHST FHDUR\n")
		file.write("%2s             %d             %d       %d               %d   %d   %d   %d   %d   %d\n" % (1, -99, -99, -99, -99, -99, -99, -99, -99, -99))

		# initial condition

		file.write("\n*INITIAL CONDITIONS\n")
		file.write("@C   PCR ICDAT  ICRT  ICND  ICRN  ICRE  ICWD ICRES ICREN ICREP ICRIP ICRID ICNAME\n")
		date = dt.datetime(self.st_yr, 3, 1)
		doy = date.strftime("%y%j")
		file.write("%2s %2s %5s %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  %d\n" % (
			1, "MZ", doy, 200, -99, 1, 1, -99, -99, -99, -99, -99, -99, -99))
		file.write("@C  ICBL  SH2O  SNH4  SNO3\n")
		file.write("%2s  %3s  %.2f  %.1f  %.1f\n" % (1, 30, 0.38, 0.5, 0.5))
		file.write("%2s  %3s  %.2f  %.1f  %.1f\n" % (1, 45, 0.38, 0.5, 0.4))
		file.write("%2s  %3s  %.2f  %.1f  %.1f\n" % (1, 60, 0.38, 0.5, 0.4))
		file.write("%2s  %3s  %.2f  %.1f  %.1f\n" % (1, 90, 0.38, 0.5, 0.3))
		file.write("%2s  %3s  %.2f  %.1f  %.1f\n" % (1, 120, 0.38, 0.5, 0.2))
		file.write("%2s  %3s  %.2f  %.1f  %.1f\n" % (1, 150, 0.38, 0.5, 0.1))

		# planting details
		file.write("\n*PLANTING DETAILS\n")
		file.write(
			"@P PDATE EDATE  PPOP  PPOE  PLME  PLDS  PLRS  PLRD  PLDP  PLWT  PAGE  PENV  PLPH  SPRL                        PLNAME\n")
		pdate = dt.datetime(self.st_yr, self.plant_month, self.plant_date)
		pdoy = pdate.strftime("%y%j")
		file.write(
			"%2s %5s  %d   %.1f    %.1f     %s     %s     %d    %d    %d    %d   %d   %d   %d   %d                      %d\n" % (
				1, pdoy, -99, 4.4, 4.4, "S", "R", 50, 0, 4, -99, -99, -99, -99, -99, -99))

		# fertilizers
		file.write("\n*FERTILIZERS (INORGANIC)\n")
		file.write("@F FDATE  FMCD  FACD  FDEP  FAMN  FAMP  FAMK  FAMC  FAMO  FOCD FERNAME\n")
		file.write(
			"%2s %5s %d  %d  %d  %d  %d  %d  %d  %d  %d\n" % (1, "FE005", -99, 10, 30, -99, -99, -99, -99, -99, -99))

		# Simulation controls
		file.write("\n*SIMULATION CONTROLS\n")

		file.write("@N GENERAL     NYERS NREPS START SDATE RSEED SNAME.................... SMODEL\n")
		num_yr = self.ed_yr - self.st_yr + 1
		sdoy = pdoy
		file.write("%2s %2s             %2s     %d     %s %5s  %d %s\n" % (1, "GE", str(num_yr), 1, "S", sdoy, 2150, "DEFAULT"))

		file.write("@N OPTIONS     WATER NITRO SYMBI PHOSP POTAS DISES  CHEM  TILL   CO2\n")
		file.write("%2s %2s              %s     %s     %s     %s     %s     %s     %s     %s     %s\n" % (1, "OP", "Y", "Y", "Y", "N", "N", "N", "N", "Y", "D"))

		file.write("@N METHODS     WTHER INCON LIGHT EVAPO INFIL PHOTO HYDRO NSWIT MESOM MESEV MESOL\n")
		file.write("%2s %2s              %s     %s     %s     %s     %s     %s     %s     %d     %s     %s     %d\n" % (1, "ME", "W", "M", "E", "R", "S", "C", "R", 1, "G", "S", 2))

		file.write("@N MANAGEMENT  PLANT IRRIG FERTI RESID HARVS\n")
		file.write("%2s %2s              %s     %s     %s     %s     %s\n" % (1, "MA", "R", "R", "R", "R", "M"))

		file.write("@N OUTPUTS     FNAME OVVEW SUMRY FROPT GROUT CAOUT WAOUT NIOUT MIOUT DIOUT VBOSE CHOUT OPOUT\n")
		file.write("%2s %2s              %s     %s     %s     %d     %s     %s     %s     %s     %s     %s     %s     %s     %s\n" % (1, "OU", "Y", "N", "A", 1, "N", "N", "N", "N", "N", "N", "Y", "N", "N"))



		file.close()
		return

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
		FILE	= file('%s'%(fileName)).readlines()		# Interact with the pyQt GUI
		#FILE	= file('%s/%s'%(self._baseDir,fileName)).readlines()
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
	
