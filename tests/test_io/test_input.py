"""
Test the read_from_file function from app.io.input.
"""

import pandas as pd
from app.io.input import read_from_file, read_csv


def test_read_from_file(tmp_path):
    file = tmp_path / "test_file.txt"
    file.write_text("Hello, world!")
    assert read_from_file(str(file)) == "Hello, world!"


def test_read_from_file_empty(tmp_path):
    file = tmp_path / "test_file_empty.txt"
    file.write_text("")
    assert read_from_file(str(file)) == ""


def test_read_from_file_multiple_lines(tmp_path):
    file = tmp_path / "test_file_lines.txt"
    file.write_text("Line 1\nLine 2\nLine 3")
    assert read_from_file(str(file)) == "Line 1\nLine 2\nLine 3"


# CSV tests


def test_read_from_file_pandas(tmp_path):
    df = pd.DataFrame({"name": ["John", "Jane"], "age": [30, 25]})
    file = tmp_path / "test_file.csv"
    df.to_csv(file, index=False)
    result = read_csv(str(file))
    pd.testing.assert_frame_equal(result, df)


def test_read_from_file_pandas_empty(tmp_path):
    df = pd.DataFrame(columns=["name", "age"])
    file = tmp_path / "test_file_empty.csv"
    df.to_csv(file, index=False)
    result = read_csv(str(file))
    pd.testing.assert_frame_equal(result, df)


def test_read_from_file_pandas_multiple(tmp_path):
    df = pd.DataFrame({"name": ["John", "Jane", "Doe"], "age": [30, 25, 35]})
    file = tmp_path / "test_file_multiple.csv"
    df.to_csv(file, index=False)
    result = read_csv(str(file))
    pd.testing.assert_frame_equal(result, df)
