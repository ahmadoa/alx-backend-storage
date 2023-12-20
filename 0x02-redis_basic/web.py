#!/usr/bin/env python3
"""5. Implementing an expiring web cache and tracker"""

from requests import get
import redis
from functools import wraps
from typing import Callable


def track_page_count(method: Callable) -> Callable:
    """tracks how many times a url was accessed"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        """inner wrapper function"""
        cache = redis.Redis()
        url = args[0]
        key = 'count:' + url
        cache.incr(key)
        page = cache.get(url)
        if page is not None:
            return page.decode('utf-8')
        page = method(*args, **kwrags)
        cache.setex(key, 10, page)
        return page
    return wrapper


def get_page(url: str) -> str:
    """obtain html content of a url & return it"""
    return get(url).text
