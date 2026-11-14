import math
import numpy as np

PI = 3.14159

def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    # 2) Perform linear regression on the detrended data.
    # 3) Predict day 15's base consumption.
    # 4) Add the day 15 fluctuation back.
    # 5) Round, then add a 5% safety margin (rounded up).
    # 6) Return the final integer.

    n = 10

    x = np.arange(1, 11)

    f = 10 * np.sin(2 * PI * x / 10)

    consumption_data = np.asarray(consumption_data)
    y = consumption_data - f

    m = (n * np.sum(x * y) - (np.sum(x))*(np.sum(y))) / (n * np.sum(x**2) - (np.sum(x))**2)

    b = (np.sum(y) - m * np.sum(x)) / n

    base_15 = m * 15 + b

    f_15 = 10 * np.sin(2 * PI * 15 / 10)

    pred_15 = base_15 + f_15

    return math.ceil(1.05 * round(pred_15))
    
