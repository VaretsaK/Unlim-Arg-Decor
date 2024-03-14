from typing import Any


def type_checker(*types: type) -> Any:
    """
    Decorator factory to check types of function parameters.

    Args:
        *types (type): Variable-length argument list of types. The decorator will ensure that
            parameters of the decorated function match these types.

    Returns:
        callable: Decorator function.

    Raises:
        TypeError: If any parameter of the decorated function does not match the specified types.
    """

    def decor(func: Any) -> Any:
        """
        Decorator function to check types of function parameters.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: Decorated function.
        """

        def inner_wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Inner wrapper function to check types of function parameters before executing the decorated function.

            Args:
                *args: Positional arguments passed to the decorated function.
                **kwargs: Keyword arguments passed to the decorated function.

            Returns:
                Any: Result of the decorated function call.
            """

            for parameter in args:
                if type(parameter) not in types:
                    raise TypeError(f"type '{type(parameter).__name__}' is not supported by this decorator.")

            print("Before function implementation")
            result = func(*args, **kwargs)
            print(f"After function implementation. Result: {result}")

            return result

        return inner_wrapper

    return decor

