import logging
from asyncio import CancelledError
from functools import wraps
from aiohttp import ContentTypeError

try:
    from urllib import parse as urlparse
except ImportError:
    # noinspection PyUnresolvedReferences
    import urlparse


__version__ = "0.1.7"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
log = logging.getLogger(__name__)


def url_maker(func):
    """
    Replacement for built-in aiohttp url maker
    Since it can't log the full url composed of query params
    """
    async def wrapper(*args, **kwargs):
        if 'url' in kwargs and 'params' in kwargs:
            kwargs['url'] = f"{kwargs['url']}?{urlparse.urlencode(kwargs.pop('params'))}"
        return await func(*args, **kwargs)
    return wrapper


def cut_none(func):
    def cut(params):
        if type(params) == dict:
            return {
                key: cut(value) for key, value in params.items() if value is not None
            }

        if type(params) == list:
            if any([type(i) == tuple for i in params]):
                return [i for i in params if i[1] is not None]

        return params
    async def wrapper(*args, **kwargs):
        return await func(*args, **cut(kwargs))
    return wrapper


def try_except_request(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ContentTypeError as e:
            log.warning(f"response is not json: {e}")
            raise
        except CancelledError as e:
            log.info(f"request cancelled: {e}")
        except Exception as e:
            log.exception(e)
    return wrapper


def prepare_repeated_params(params: list, repeated_values: dict):
    for key, values in repeated_values.items():
        if values is not None:
            values = values if type(values) == list else [values]
            for value in values:
                params.append((key, value))
