from functools import lru_cache

class Something():

    @lru_cache(maxsize = None)
    def recursive():
        