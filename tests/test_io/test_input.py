"""
Test the read_from_file function from app.io.input.
"""

from app.io.input import read_from_file


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
