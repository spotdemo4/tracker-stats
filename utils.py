import re

def parseCookieFile(cookiefile):
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies = {}
    with open(cookiefile, 'r') as fp:
        for line in fp:
            if not line.startswith('# ') and len(line.strip()) > 0:
                lineFields = re.findall(r'[^\s]+', line) #capturing anything but empty space
                try:
                    cookies[lineFields[5]] = lineFields[6]
                except Exception as e:
                    print(e)
          
    return cookies