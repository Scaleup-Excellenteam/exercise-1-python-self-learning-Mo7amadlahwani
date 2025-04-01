"""
Module for measuring the execution time of functions.
This module provides a function `running_2000` that measures the time it takes to execute another function.

Function:
- `running_2000(f, *args, **kwargs)`: Measures and returns the execution time of a given function `f` with the provided arguments.
"""
import time


def running_2000(f, *args,**kwargs):
    """
        Measures the execution time of the provided function `f`.

        Parameters:
        - f (function): The function whose execution time needs to be measured.
        - *args: The positional arguments to be passed to the function.
        - **kwargs: The keyword arguments to be passed to the function.

        Returns:
        - float: The time (in seconds) it took to execute the function `f`.
        """
    start_time = time.time()  # Record the start time
    f(*args, **kwargs)  # Call the function with its arguments
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    return elapsed_time


if __name__=="__main__":
    running_2000(print)
