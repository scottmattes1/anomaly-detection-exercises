import pandas as pd



############### GET LOWER UPPER BOUNDS FUNCTION ###############

def get_lower_upper_bounds(series, coeff):
    """
    This function returns the upper and lower bound values for outliers. It takes in a series argument and a multiplier (coeff)
    argument and computes the lower and upper bound off of iqr manipulation proportional to the multiplier. Outputs the lower
    and upper bound values
    """
    q1 = series.quantile(.25)
    q3 = series.quantile(.75)
    iqr = q3 - q1
    lower_bound = q1 - (coeff * iqr)
    upper_bound = q3 + (coeff * iqr)
    
    return lower_bound, upper_bound