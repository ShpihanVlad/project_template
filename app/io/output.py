"""
Module for outputting data to console, file or csv file.
"""

from typing import Optional
import pandas as pd


def write_to_console(data):
    """
    Function for outputting data to console.
    :param data: data to print. For informative output should support __str__ or __repr__ methods.
    :return: None
    """
    print(data)


def write_to_file(filename, data, mode="w", encoding="utf-8"):
    """
    Function for writing data to file. Overwrites file if exists by default.
    :param filename: a file to write to.
    :param data: text to write.
    :param mode: mode of opening file. Default is "w".
    :param encoding: encoding of the file. Default is utf-8.
    :return: None
    """
    with open(filename, mode, encoding=encoding) as file:
        file.write(data)


def write_csv(filename, data: pd.DataFrame, **kwargs) -> Optional[str]:
    """
    Function for writing data to csv file using pandas. Overwrites csv file if exists by default.
    :param filename: a path to the csv file. If None, returns a string, as in pandas specification.
    :param data: DataFrame to write to csv file
    :param kwargs: arguments for pandas.to_csv function
    :return: CSV string if filename is None, None otherwise
    """
    return data.to_csv(filename, **kwargs)
