# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    estimatePrice.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pmasson <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/26 14:16:28 by pmasson           #+#    #+#              #
#    Updated: 2019/03/26 16:44:16 by pmasson          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import signal
import utils
import os
import numpy as np

signal.signal(signal.SIGINT, utils.close_prog)

def get_mileage():
    stop = 0
    while (stop == 0):
        com = raw_input("Enter a mileage please : ")
        if (com.lower() == "q"):
            sys.exit(0)
        try:
            mileage = float(com)
            if (mileage < 0):
                print("Error, mileage can't be negative")
            stop = 1
        except ValueError:
            print("Error, not a valid mileage")
    return (mileage)

def get_thetas():
    if (os.path.isfile(utils.thetaFile) == True):
        try:
            with open(utils.thetaFile, "r") as tfile:
                rfile = tfile.read()
                lfile = utils.manage_file(rfile, "=")
                try:
                    if (len(lfile) != 4):
                        raise ValueError
                    thetas = np.array([[float(lfile[1])], [float(lfile[3])]])
                except ValueError:
                    print("Error values in thetas file")
                    sys.exit(0)
        except IOError:
            print("Error, no reading rights on thetas file")
            sys.exit(0)
    else:
        thetas = np.array([[0],[0]])
    return (thetas)

def get_price(mileage, thetas):
    mileageArray = np.array([[1],[mileage]])
    ret = np.vdot(thetas, mileageArray)
    print("The price estimated for a mileage of {} kilometers is : {} euros"\
            .format(mileage, ret))

def estimate_price():
    mileage = get_mileage()
    thetas = get_thetas()
    get_price(mileage, thetas)

if __name__ == "__main__":
    estimate_price()
