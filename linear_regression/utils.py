import sys
import numpy as np
import matplotlib.pyplot as plt

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
    return (x, mu, sigma)

def draw_points(x, y, theta, mu, sigma):
    a1 = theta[0,0] * 1 + theta[1, 0] * (1000 - mu) / sigma
    a2 = theta[0,0] * 1 + theta[1, 0] * (240000 - mu) / sigma
    plt.scatter(x[:,1], y)
    plt.plot([1000, 240000], [a1, a2], color="r")
    plt.show()
