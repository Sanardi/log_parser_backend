# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:23:22 2020

@author: bla
"""

# importing unittest module
import unittest
import pandas as pd

# unittest will test all the methods whose name starts with 'test'
class SampleTest(unittest.TestCase):
   # return True or False
   def test(self):
      #self.assertTrue(True)
      self.assertFalse(False)
      
      
class TestLogFile(unittest.TestCase):
    logfile = pd.read_table("input-file-10000.txt", delim_whitespace=True, header=None)
    logfile.columns = ["Timestamp", "hostname1", "hostname2"]
    timelog = logfile["Timestamp"]
    #print(logfile.head())


    def test_log_format(self):
        
        
        timelog = self.logfile["Timestamp"]
        timelog = self.timelog
        print(timelog.dtypes)
        self.assertTrue(timelog.dtypes == "int64")
        self.assertFalse('Foo'.isupper())

    def test_valid_date(self):
        timelog = self.timelog
        self.assertTrue(0 < int(timelog[0]) < 1565733598341)
            
            
# running the test
unittest.main()