from typing import Any, Callable, TypeVar, Type, Optional, Generic

T = TypeVar('T')


class PyOptional(Generic[T]):

	@classmethod
	def empty(cls):
		return PyOptional(None)

	def __init__(self, obj: Optional[T]) -> None:
		self.value = obj

	def get(self) -> Optional[T]:
		return self.value

	def or_else(self, default: T) -> T:
		return self.value or default

	def or_else_do(self, _lambda: Callable) -> T:
		if self.value:
			return self.value
		else:
			return _lambda()

	def or_raise(self, exception: Type[Exception]) -> T:
		if self.value:
			return self.value
		else:
			raise exception

	def is_present(self) -> bool:
		if self.value is not None:
			return True

		return False

	def is_absent(self) -> bool:
		return self.value is None

	def if_present(self, _lambda: Callable, default: T) -> Any:
		if self.is_present():
			return _lambda(self.value)
		else:
			return default

	def if_present_or_raise(self, _lambda: Callable, exception: Type[Exception]) -> Any:
		if self.is_present():
			return _lambda(self.value)
		else:
			raise exception
