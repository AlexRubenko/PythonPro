from collections import OrderedDict
from memory_profiler import profile
import functools
import requests


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                # переносимо в кінець списку
                deco._cache.move_to_end(cache_key, last=True)
                deco._cache[cache_key][1] += 1  # збільшуємо лічильник використання
                return deco._cache[cache_key][0]
            result = f(*args, **kwargs)
            # видаляємо, якщо досягли ліміта
            if len(deco._cache) >= max_limit:
                lfu_key = min(deco._cache, key=lambda k: deco._cache[k][1])  # знаходимо ключ з найменшим лічильником
                deco._cache.pop(lfu_key)
            deco._cache[cache_key] = [result, 1]  # зберігаємо результат та лічильник використання
            return result
        deco._cache = OrderedDict()
        return deco
    return internal

@profile
@cache(max_limit=10000)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


content = fetch_url("https://en.wikipedia.org/wiki/Python_(programming_language)")  # виконується запит
content = fetch_url("https://en.wikipedia.org/wiki/Python_(programming_language)")  # результат отримується з кешу
content = fetch_url("https://en.wikipedia.org/wiki/Python_(programming_language)")  # результат отримується з кешу
content = fetch_url("https://en.wikipedia.org/wiki/Linux)")  # виконується запит