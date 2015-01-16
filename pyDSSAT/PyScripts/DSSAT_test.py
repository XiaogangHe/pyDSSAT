#!/usr/bin/env python

import unittest
import numpy as N
import DSSAT_LIBRARY as DL
import os
import random
#from   pylab	import	*

class TestDSSAT(unittest.TestCase):

    def test_Input_year(self):
	os.system('rm *.v45 *.GSX *.OUT')
        DL.File(crop='Maize',weather='DTCM',st_yr=1948,ed_yr=2010,plant_month=6,plant_date=10,mode='S')
        model = DL.Model('S','run.v45','../DSCSM045.CTR')
        model.run()
        out = DL.postProcess('../', 'POST-VAR-INFO.CDE')
        [start_year, end_year] = out.getVarValues('./Summary.OUT')[1:3]
        self.assertEqual(start_year, 1948)
        self.assertEqual(end_year-1, 2010)

    def test_Input_crop1(self):
	os.system('rm *.v45 *.GSX *.OUT')
        DL.File(crop='Wheat',weather='DTCM',st_yr=1948,ed_yr=2010,plant_month=6,plant_date=10,mode='S')
        model = DL.Model('S','run.v45','../DSCSM045.CTR')
        model.run()
        out = DL.postProcess('../', 'POST-VAR-INFO.CDE')
        cropType = out.getVarValues('./Summary.OUT')[3]
        self.assertEqual(cropType, 'WH')
	
    def test_Input_crop2(self):
	os.system('rm *.v45 *.GSX *.OUT')
        DL.File(crop='Maize',weather='DTCM',st_yr=1948,ed_yr=2010,plant_month=6,plant_date=10,mode='S')
        model = DL.Model('S','run.v45','../DSCSM045.CTR')
        model.run()
        out = DL.postProcess('../', 'POST-VAR-INFO.CDE')
        cropType = out.getVarValues('./Summary.OUT')[3]
        self.assertEqual(cropType, 'MZ')

    def test_Model_S(self):
        os.system('./DSCSM045.EXE S run.v45 ../DSCSM045.CTR')
        os.system('mv Summary.OUT Summary_ref.OUT')
	os.system('rm *.v45 *.GSX')

        DL.File(crop='Maize',weather='DTCM',st_yr=1948,ed_yr=2010,plant_month=6,plant_date=10,mode='S')
        model = DL.Model('S','run.v45','../DSCSM045.CTR')
        model.run()
        
        out = DL.postProcess('./', 'SUMMARYOUT.CDE')
        rand_variable1 = random.randint(0,60)
        rand_variable2 = random.randint(0,60)
        
        output = out.getVarValues('./Summary.OUT')[0]
        output_ref = out.getVarValues('./Summary_ref.OUT')[0]
        varName1 = output.keys()[rand_variable1]
        varName2 = output.keys()[rand_variable2]
        N.testing.assert_array_almost_equal(output[varName1], output_ref[varName1])
        N.testing.assert_array_almost_equal(output[varName2], output_ref[varName2])

if __name__ == "__main__":
    unittest.main()
