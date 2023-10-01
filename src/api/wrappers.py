import logging
from typing import Type, Callable, TypeVar

from pydantic import ValidationError

logger = logging.getLogger(__name__)

T = TypeVar('T')
V = TypeVar('V')
K = TypeVar('K')


def api_wrapper(schema: Type[T]):
    def decorator(api_method: Callable[[V, T, ...], K]):
        def wrapper(cls: V, request: Type[T], **kwargs):
            try:
                schema.model_validate(request)
                result = api_method(cls, request, **kwargs)
            except ValidationError:
                logger.exception(f'during validation {request=} an exception occured')
                raise
            except Exception:
                logger.exception(f'during {api_method.__name__} an exception occurred')
                raise
            logger.info(f'response {api_method.__name__} with {result}')
            return result

        return wrapper

    return decorator
