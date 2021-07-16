import numpy as np


# Q = 2
# f = 10000
# gm = 0.00187041
# R = 55000
# Gm = gm - 1/R
# Rfilter = 1/(gm - 1/20000)
# print(Rfilter)

# wn = 2*np.pi*f
# print("With load")
# print("Rhi: ", 1/(gm-Gm))
# print("C1: ", Q*1e6/(Rfilter*wn), "uF")
# print("C2: ", 1e6*pow(Gm, 2)*Rfilter/(Q*wn), "uF")
# print("Gain at wn:", Gm*Rfilter)
# print("\n")
# print("Without load")
# print("C1: ", Q*1e6/(Rfilter*wn), "uF")
# print("C2: ", 1e6*pow(gm, 2)*Rfilter/(Q*wn), "uF")
# print("Gain at wn:", gm*Rfilter)

gm = 0.00187041
Rt = 66000
wn = 2*np.pi*10000
Q = 2

print('R: ', 1/(gm*(1-1/Q) + 1/(Q*Rt)))
print('C:', (gm-1/Rt)/wn)