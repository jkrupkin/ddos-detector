import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-v',help="Verbose mode: Print all activity on the command line",action="store_true")
group.add_argument('-q',help="Quiet mode: run program as a daemon", action="store_true")
parser.add_argument('-g',help="Display a time series or bar graph")

parser.parse_args()

