__author__ = 'lpeng'
# # import library
##---------------
import sys, os, glob, gc, csv
# tool
import numpy as np
from pylab import *
import datetime as dt

gc.collect()


class File():
	def __init__(self, crop='maize', weather='DTCM', st_yr=1948, ed_yr=2012, plant_month=6, plant_date=10, mode='S'):

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
		if self.crop == "maize":
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
