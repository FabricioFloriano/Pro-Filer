from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date
from unittest.mock import patch, Mock
import pytest
import tempfile
import os


def new_temp_file(content, file_extension=".txt"):
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, "temp_file" + file_extension)
    with open(temp_file, "w") as file:
        file.write(content)
    return temp_file


@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {
                "base_path": new_temp_file(
                    "This is the content of the file.", ".txt"
                )
            },
            "File name: temp_file.txt\n"
            "File size in bytes: 32\n"
            "File type: file\n"
            "File extension: .txt\n"
            f"Last modified date: {date.today()}\n",
        ),
        (
            {
                "base_path": new_temp_file(
                    "This is the content of the file.", ""
                )
            },
            "File name: temp_file\n"
            "File size in bytes: 32\n"
            "File type: file\n"
            "File extension: [no extension]\n"
            f"Last modified date: {date.today()}\n",
        ),
        ({"base_path": "/home/trybe/????"}, "File '????' does not exist\n"),
    ],
)
def test_show_details(capsys, context, expected):
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected


context = {"base_path": "/path/to/your/file"}


def test_show_details_does_not_exist(capsys):
    with patch("os.path.exists", Mock(return_value=False)):
        show_details(context)

    captured = capsys.readouterr()
    expected_output = "File 'file' does not exist\n"
    assert captured.out == expected_output
