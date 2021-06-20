import hashlib

SALT = "my_salt"
HASH_TABLE = {}


def cache_web(url):
    if HASH_TABLE.get(url):
        print(f'{url} is on the cache')
    else:
        res = hashlib.sha256(SALT.encode() + url.encode()).hexdigest()
        HASH_TABLE[url] = res


cache_web('https://www.google.com/')
cache_web('https://github.com/')
cache_web('https://www.google.com/')
