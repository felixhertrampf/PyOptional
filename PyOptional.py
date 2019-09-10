from typing import Any, Callable, TypeVar, Type, Optional


class PyOptional(Optional):
	T: TypeVar = TypeVar("T")
	Optional = Callable[[T], Any]

	def __init__(self, obj: T):
		self.value: Any = obj

	def get(self) -> Optional[T]:
		return self.value

	def or_else(self, default: T) -> T:
		return self.value or default

	def or_else_do(self, _lambda: Callable) -> Any:
		if self.is_present():
			return self.value
		else:
			return _lambda()

	def or_raise(self, exception: Type[Exception]) -> T:
		if self.is_present():
			return self.value
		else:
			raise exception

	def is_present(self) -> bool:
		return self.value is not None

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
