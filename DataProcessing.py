import pandas as pd
import numpy as np


def read_data(path):
    """
    This function reads the csv file from the path given and returns a DataFrame object
    :param path:
    :return DataFrame:
    """
    return pd.read_csv(path)


class PreProcessing:
    """
    This class is used for preprocessing
    """
    def __int__(self, path):
        np.random.seed(42)
        self.pima_df = read_data(path)

    def null_handler(self):
        pass
