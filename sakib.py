import string
import random
urlList = {}


def encode(longUrl):
    """Encodes a URL to a shortened URL.

    :type longUrl: str
    :rtype: str
    """
    tinyurl = ""
    while True:
        tinyurl = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(6))
        if tinyurl not in urlList:
            urlList[tinyurl] = longUrl
            break
    return tinyurl


print(encode('google.com'))