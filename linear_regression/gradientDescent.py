# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradientDescent.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmasson <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/26 14:16:32 by pmasson           #+#    #+#              #
#    Updated: 2019/03/27 15:02:26 by pmasson          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
import signal
import utils
import os

signal.signal(signal.SIGINT, utils.close_prog)

def get_data():
    x = list()
    y = list()
    if (os.path.isfile(utils.dataFile) == False):
        print("Error, no data file")
        sys.exit(0)
    else:
        try:
            with open(utils.dataFile, "r") as datafile:
                rdata = datafile.read()
                ldata = utils.manage_file(rdata, ",")
                i = 2
                if (len(ldata) % 2 != 0):
                    print("Error, wrong number of data")
                    sys.exit(0)
                while (i < len(ldata)):
                    try:
                        x.append([1, float(ldata[i])])
                        y.append([float(ldata[i + 1])])
                        i = i + 2
                    except ValueError:
                        print("Error, wrong value in data")
                        sys.exit(0)
        except IOError:
            print("Error, no reading rights on data file")
            sys.exit(0)
    x1 = np.asarray(x)
    y1 = np.asarray(y)
    return (x1, y1)

def cost(theta, x, y):
    m = len(x)
    if (m == 0):
        print("Error, no data to make gradient descent")
        sys.exit(0)
    try:
        j = np.sum((np.dot(x, theta) - y)**2) * 2 / m
    except FloatingPointError:
       print("an error occured, try changing alpha value")
       sys.exit(0)
    return (j)



def gradient(x,y):
    alpha = utils.alpha
    m = len(x)
    if (m == 0):
        print("Error, no data to make gradient descent")
        sys.exit(0)
    dj = 1
    theta = np.array([[1],[1]])
    while (dj > 0.1):
        j1 = cost(theta, x, y)
        tmp0 = theta[0, 0] - np.vdot((np.dot(x,theta) - y).T, x[:,0]) * alpha / m
        tmp1 = theta[1, 0] - np.vdot((np.dot(x,theta) - y).T, x[:,1]) * alpha /  m
        theta = np.array([[tmp0], [tmp1]])
        j = cost(theta, x, y)
        dj = abs(j1 - j)
    return (theta)

def write_theta(theta):
    ret = str()
    ret = "theta0 = " + str(theta[0, 0]) + "\n" + "theta1 = " + str(theta[1, 0])
    try: 
        with open(utils.thetaFile, "w") as tfile:
            tfile.write(ret)
    except IOError:
        print("Error, no writting rights on thetas file")
        sys.exit(0)

def gradient_descent():
    np.seterr(all='raise')
    x, y = get_data()
    x = utils.normalize(x)
    theta = gradient(x,y)
    write_theta(theta)


if __name__ == "__main__":
    gradient_descent()
