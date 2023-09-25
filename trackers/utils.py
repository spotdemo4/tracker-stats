import re

def normalizeSize(num_unit):
    num, b, c = re.split(r'([a-z])', num_unit, 1, flags=re.I)
    num = float(num.strip())
    unit = (b + c).strip().upper()

    if unit == 'MIB':
        num *= 1.049
        unit = 'MB'
    elif unit == 'GIB':
        num *= 1.074
        unit = 'GB'
    elif unit == 'TIB':
        num *= 1.1
        unit = 'TB'
    
    return '{:.2f} '.format(num) + unit

def normalizeFloat(float_str):
    try:
        return '{:.2f}'.format(float(float_str.replace(',', '')))
    except ValueError:
        return '0.00'

def normalizeInt(int_str):
    try:
        return '{:.0f}'.format(float(int_str.replace(',', '')))
    except ValueError:
        return '0'