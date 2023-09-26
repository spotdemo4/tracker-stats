import re, os

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

def getUserAgent():
    if os.path.isfile('./cookies/useragent.txt'):
        with open('./cookies/useragent.txt', 'r') as fp:
            return fp.read().strip()
    else:
        return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'

def setUserAgent(user_agent):
    with open('./cookies/useragent.txt', 'w') as fp:
        fp.write(user_agent)