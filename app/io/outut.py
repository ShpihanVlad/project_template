"""
Module for outputting data to console, file or csv file.
"""

from typing import Optional
import pandas as pd


def write_to_console(data):
    pass


def write_to_file(filename, data, mode="w", encoding="utf-8"):
    pass


def write_csv(filename, data: pd.DataFrame, **kwargs):
    pass
