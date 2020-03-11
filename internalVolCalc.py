# internalVolCalc.py
import pandas as pd
import numpy as np
from math import pi


def readFile(t_input_file_name):
    df = pd.read_csv(t_input_file_name)
    cols = list(df.columns)
    x = df[cols[0]]
    y = df[cols[1]]
    return (x, y)


def internalVolCalc(t_x, t_y):
    volAccum = 0
    for i in range(1, len(t_x)):
        dx = t_x[i-1] - t_x[i]
        D = 2*t_y[i-1]
        d = 2*t_y[i]

        # V = pi * h / 12 * (D**2 + D*d + d**2)
        volAccum += pi * dx * (D**2 + D*d + d**2)/12
    return volAccum


if __name__ == "__main__":
    fileName = input("Enter file name: ")
    vol = internalVolCalc(*readFile(fileName))
    print("Volume: {:.16f}".format(vol))
