import sys
import numpy as np

thetaFile = "thetas"
dataFile = "data.csv"
alpha = 0.3

def close_prog(signal, frame):
    sys.exit(0)

def manage_file(rfile, c):
    rfile = rfile.replace(" ", "")
    rfile = rfile.replace("\n", " ")
    rfile = rfile.replace(c, " ")
    rfile = rfile.strip()
    lfile = rfile.split()
    return (lfile)

def normalize(x):
    mu = np.sum(x[:, 1]) / len(x)
    sigma = np.std(x[:,1])
    x[:,1] = (x[:,1] - mu) / sigma
    return (x)
