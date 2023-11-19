from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_inexistent_file():
    context = {
        "all_files": ["non_existent_file1.txt", "non_existent_file2.txt"]
    }

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)


def test_find_duplicate_files_empty():
    context = {"all_files": []}

    assert find_duplicate_files(context) == []


def test_show_disk_usage_expected(monkeypatch, tmp_path, capsys):
    file1 = tmp_path / "teste.txt"
    file2 = tmp_path / "teste1.txt"
    file1.write_text("hello!")
    file2.write_text("hello word!")
    file1_path = str(file1)
    file2_path = str(file2)
    context = {"all_files": [file1_path, file2_path]}
    assert find_duplicate_files(context) == []
