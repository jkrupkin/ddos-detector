#!/usr/bin/env python3
#import argparse
import sniffer as s
import time
import ai
import grapher
import numpy as np 
import stats
import matplotlib as mpl
import matplotlib.pyplot as npl
#parser = argparse.ArgumentParser()
#group = parser.add_mutually_exclusive_group()
#group.add_argument('-v',help="Verbose mode: Print all activity on the command line",action="store_true")
#group.add_argument('-q',help="Quiet mode: run program as a daemon", action="store_true")
#parser.add_argument('-g',help="Display a time series or bar graph")

#parser.parse_args()
#print("Starting packet sniffer")
#s.start_sniffer()
#print("Capturing packets for 30s")
#time.sleep(30)
#print("Stopping sniffer")
#s.stop_sniffer()
#print("Dumping file for analysis")
#s.analysis_output()
print("Loading AI model")
mod = ai.model("ai_model.h5")
dataset = ai.dataset("analysis_output_2.csv")
dataformat = ai.dataformat(dataset)
print("predicting results")
results = ai.predict(dataformat[0], mod)
#print(results.shape)
stats.conf(dataformat[0])

