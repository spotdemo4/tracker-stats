import re
import math

def convertSize(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

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
    if float(float_str) < 0:
        return '0.00'
    
    try:
        return '{:.2f}'.format(float(str(float_str).replace(',', '')))
    except ValueError:
        return '0.00'

def normalizeInt(int_str):
    if int(int_str) < 0:
        return '0'
    
    try:
        return '{:.0f}'.format(float(str(int_str).replace(',', '')))
    except ValueError:
        return '0'