from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {
                "all_files": [
                    "file1",
                    "file2",
                    "file3",
                    "file4",
                    "file5",
                    "file6",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            "Found 6 files and 2 directories\n"
            "First 5 files: ['file1', 'file2', 'file3', 'file4', 'file5']\n"
            "First 5 directories: ['src', 'src/utils']\n",
        ),
        (
            {"all_files": [], "all_dirs": []},
            "Found 0 files and 0 directories\n",
        ),
    ],
)
def test_show_preview(capsys, context, expected):
    show_preview(context)
    captured = capsys.readouterr()

    assert captured.out == expected


# @pytest.mark.parametrize(
# "context", "expected",
#     [
#         (
#             {
#                 "all_files": [
#                     "file1",
#                     "file2",
#                     "file3",
#                     "file4",
#                     "file5",
#                     "file6",
#                 ],
#                 "all_dirs": ["src", "src/utils"],
#             },
#             "Found 6 files and 2 directories\n",
#             "First 5 files: ['file1', 'file2', 'file3', 'file4', 'file5']\n"
#             "First 5 directories: ['src', 'src/utils']\n",
#         ),
#         (
#             {"all_files": [], "all_dirs": []},
#             "Found 0 files and 0 directories\n",
#         ),
#     ],
# )
