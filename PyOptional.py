from typing import Callable, TypeVar, Type, Optional, Generic

T = TypeVar('T')


class PyOptional(Generic[T]):
    value: T

    @classmethod
    def empty(cls):
        return PyOptional[T](None)

    def __init__(self, value: Optional[T]) -> None:
        self.value = value

    def get(self) -> Optional[T]:
        return self.value

    def or_else(self, default: T) -> T:
        return self.value or default

    def or_else_do(self, _lambda: Callable) -> T:
        if self.value:
            return self.value
        else:
            return _lambda()

    def or_raise(self, exception: Exception) -> T:
        if self.value:
            return self.value
        else:
            raise exception

    def is_present(self) -> bool:
        return self.value is not None

    def is_none(self) -> bool:
        return self.value is None

    def if_present(self, _lambda: Callable, default: T) -> T:
        if self.is_present():
            return _lambda(self.value)
        else:
            return default

    def if_present_or_raise(self, _lambda: Callable, exception: Exception) -> T:
        if self.is_present():
            return _lambda(self.value)
        else:
            raise exception
