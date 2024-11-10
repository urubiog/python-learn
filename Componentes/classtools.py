from typing import Any, Dict, Sequence, Sized, Type, Union, Callable
from inspect import signature, getmembers


class Tool:
    def __init__(self) -> None:
        self._info = ""

    @property
    def info(self) -> str:
        """Gets the info value."""
        return self._info

    @info.setter
    def info(self, value: str) -> None:
        """Function to attach a value to self.info."""
        if not isinstance(value, str):
            raise ValueError("Expected info to be str.")

        self._info = value


class Verifiers(Tool):
    """Class representing uniform verifiers for objects."""

    def __init__(self) -> None:
        super().__init__()
        self.info = "Meant to be used to simplify commonly used conditionals."

    @staticmethod
    def verify_type(obj: object, etype: Union[type, tuple[type, ...]]) -> Any:
        """Verifies if var is an instance of given type"""
        if not isinstance(obj, etype):
            raise ValueError(f"Expected {obj} to be {etype}.")

        return obj

    @staticmethod
    def verify_length(obj, elength: int) -> Any:
        if not len(obj) == elength:
            raise IndexError(f"Expected {obj} to be {elength} in length.")

        return obj

    @staticmethod
    def verify_indexable(obj: object) -> Any:
        """
        Check if an object is indexable (has __getitem__ method).

        Args:
            obj (Any): The object to check.

        Returns:
            bool: True if the object is indexable, False otherwise.
        """
        if not hasattr(obj, "__getitem__") and callable(getattr(obj, "__getitem__")):
            raise IndexError("Not supported.")

        return obj

    @staticmethod
    def verify_components_type(obj, etype: type) -> Any:
        """
        Check if an object has the correct containing type.
        Object must have __len__ and __getitem__ methods defined.

        Args:
            obj (Any): The object to check.
            etype type: The expected components type.

        Returns:
            None
        """
        for i in range(len(obj)):
            if type(obj[i]) != etype:
                raise ValueError(f"Expected {obj} to have {etype} components.")

        return obj


class Testers(Tool):
    def __init__(self) -> None:
        super().__init__()
        self.info = "Meant to be used to simplify testing a new class."
        self.__dependencies = ["re", "inspect"]
        self.__import_dependencies()

    def __import_dependencies(self) -> None:
        for module_name in self.__dependencies:
            try:
                # Import the module
                __import__(module_name)
            except ImportError as e:
                print(f"[!] Error: {e}")

    @staticmethod
    def test_methods(clss: Type):
        raise NotImplemented
        # Acceding class methods

        # Verifing if methods are Callable

        # Removing special attributes

        # Creating a personalized test for every method depending on arguments types
        pass

    @staticmethod
    def test_method(func: Callable, n: int = 5) -> bool:
        raise NotImplemented
        Verifiers.verify_type(n, int)
        if not callable(func):
            raise TypeError("Expected callable argument for func.")

        # Obtaining func signature
        sign = signature(func)

        # Looping through parameters and annotations
        args = {
            param_name: param.annotation
            for param_name, param in sign.parameters.items()
        }

        print(args)

        # Print errors

        return False
