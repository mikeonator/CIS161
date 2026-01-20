#Michael Audi - CIS161 Week 3 Extra Credit Life Expectancy

import datetime

life_table = {
    0: 0.006064,
    1: 0.000491,
    2: 0.000309,
    3: 0.000248,
    4: 0.000199,
    5: 0.000167,
    6: 0.000143,
    7: 0.000126,
    8: 0.000121,
    9: 0.000121,
    10: 0.000127,
    11: 0.000143,
    12: 0.000171,
    13: 0.000227,
    14: 0.000320,
    15: 0.000451,
    16: 0.000622,
    17: 0.000826,
    18: 0.001026,
    19: 0.001182,
    20: 0.001301,
    21: 0.001404,
    22: 0.001498,
    23: 0.001586,
    24: 0.001679,
    25: 0.001776,
    26: 0.001881,
    27: 0.001985,
    28: 0.002095,
    29: 0.002219,
    30: 0.002332,
    31: 0.002445,
    32: 0.002562,
    33: 0.002653,
    34: 0.002716,
    35: 0.002791,
    36: 0.002894,
    37: 0.002994,
    38: 0.003091,
    39: 0.003217,
    40: 0.003353,
    41: 0.003499,
    42: 0.003642,
    43: 0.003811,
    44: 0.003996,
    45: 0.004175,
    46: 0.004388,
    47: 0.004666,
    48: 0.004973,
    49: 0.005305,
    50: 0.005666,
    51: 0.006069,
    52: 0.006539,
    53: 0.007073,
    54: 0.007675,
    55: 0.008348,
    56: 0.009051,
    57: 0.009822,
    58: 0.010669,
    59: 0.011548,
    60: 0.012458,
    61: 0.013403,
    62: 0.014450,
    63: 0.015571,
    64: 0.016737,
    65: 0.017897,
    66: 0.019017,
    67: 0.020213,
    68: 0.021569,
    69: 0.023088,
    70: 0.024828,
    71: 0.026705,
    72: 0.028761,
    73: 0.031116,
    74: 0.033861,
    75: 0.037088,
    76: 0.041126,
    77: 0.045241,
    78: 0.049793,
    79: 0.054768,
    80: 0.060660,
    81: 0.067027,
    82: 0.073999,
    83: 0.081737,
    84: 0.090458,
    85: 0.100525,
    86: 0.111793,
    87: 0.124494,
    88: 0.138398,
    89: 0.153207,
    90: 0.169704,
    91: 0.187963,
    92: 0.208395,
    93: 0.230808,
    94: 0.253914,
    95: 0.277402,
    96: 0.300882,
    97: 0.324326,
    98: 0.347332,
    99: 0.369430,
    100: 0.391927,
    101: 0.414726,
    102: 0.437722,
    103: 0.460800,
    104: 0.483840,
    105: 0.508032,
    106: 0.533434,
    107: 0.560105,
    108: 0.588111,
    109: 0.617516,
    110: 0.648392,
    111: 0.680812,
    112: 0.714852,
    113: 0.750595,
    114: 0.788125,
    115: 0.827531,
    116: 0.868907,
    117: 0.912353,
    118: 0.957970,
    119: 1.000000
    }

def life_expectancy(age:int):
    '''
    Input an integer representing someone's numerical age between 0 and 119, and the function will output (based on the current year)
    that person's projected date of death (based on the "Period Life Table, 2022, as used in the 2025 Trustees Report"
    accessible on the Social Security Administration Website)
    
    :param age: An integer representing someone's numerical age.
    :type age: int
    '''
    
    now = datetime.datetime.now()
    current_year = now.year
    surviv = 1
    expec = 0

    #range check
    if age < 0 or age > 119:
        return False
    
    #Calculate Life Expectancy by iterating through the imported Life Table dictionary
    for key, value in life_table.items():
        #by combining survival probability year by year, one can calculate the number of years one most likely has left
        if key >= age:
            surviv *= (1 - value)
            expec += surviv
    return (current_year + int(expec))
