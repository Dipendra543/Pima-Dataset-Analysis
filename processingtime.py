import time

# Decorator to calculate the running time of any function


def calculate_running_time(func):
    """
    This function is used to calculate the running time of any other function and can be used as a decorator
    :param func:
    :return:
    """
    def helper(*args, **kwargs):
        """
        A helper function to calculate the actual time taken
        :param args:
        :param kwargs:
        :return:
        """
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()

        print("Total Time Taken to Run: ", func.__name__, end - begin, "ms", "\n")

    return helper

