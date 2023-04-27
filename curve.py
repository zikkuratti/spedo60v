import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# discharge time in hours
#t = np.array([0, 1, 1.15, 1.5, 2.15, 3, 3.1])
t = np.array([0, 1, 1.15, 1.5, 2.15, 3])
# battery voltage in volts
#v = np.array([67.2, 61.5, 60.5, 58.4, 57.8, 54.4, 48])
v = np.array([67.2, 61.5, 60.5, 58.4, 57.8, 54.4])
# exponential function
def exp_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# logarithmic function
def log_func(x, a, b, c):
    return a * np.log(b * x) + c

# fit data to exponential function
exp_params, exp_covariance = curve_fit(exp_func, t, v, maxfev=100000)

# fit data to logarithmic function
log_params, log_covariance = curve_fit(log_func, t, v, maxfev=100000)

# plot original data
plt.plot(t, v, 'ko', label="Voltage in current time")

# plot exponential curve
plt.plot(t, exp_func(t, *exp_params), 'r-', label="Exponential Fit")

# plot logarithmic curve
plt.plot(t, log_func(t, *log_params), 'b--', label="Logarithmic Fit")

# add legend and labels
plt.legend()
plt.xlabel("Discharge Time (hours)")
plt.ylabel("Battery Voltage (volts)")
plt.show()
