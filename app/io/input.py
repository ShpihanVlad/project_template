"""
Module for input data from console or file with support for csv using pandas.
"""

import pandas as pd


def input_from_console(prompt="Write data: ") -> str:
    """
    Function for asking to input data from console.
    :param prompt: text to show before input
    :return: inputed by user text
    """
    text = input(prompt)
    return text


def read_from_file(filename, encoding="utf-8") -> str:
    """
    Function for reading data from file.
    :param filename: a file to read from. Should be compatible with open() function.
    :param encoding: encoding of the file. Default is utf-8.
    :return:
    """
    with open(filename, "r", encoding=encoding) as file:
        data = file.read()
    return data


def read_csv(filename, **kwargs) -> pd.DataFrame:
    """
    Function for reading csv file using pandas.
    :param filename: a path to the csv file
    :param kwargs: arguments for pandas.read_csv function
    :return: DataFrame with data from csv file
    """
    data = pd.read_csv(filename, **kwargs)
    return data
