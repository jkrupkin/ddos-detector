import numpy as np
import scipy.stats

def conf(data, confidence=0.95):
    mean = data.mean()
    std = data.std()
    resulto = []
    lower = mean - std*1.96
    upper = mean + std*1.96

    print("lower: ", lower)
    print("upper: ", upper)
