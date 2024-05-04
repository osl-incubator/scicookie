"""Tool for fixing the end of file."""

from pathlib import Path

from pre_commit_hooks import end_of_file_fixer


def is_binary(file_path) -> bool:
    """Check if the given file is binary."""
    try:
        with open(file_path, "rb") as file:
            textchars = bytearray(
                {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F}
            )
            return bool(file.read(1024).translate(None, textchars))
    except Exception as e:
        print(f"Error opening file {file_path}: {e}")
        return True


def run(dir_path: Path) -> None:
    """Fix the end of file for all files recursively inside a directory."""
    base_path = dir_path.absolute()
    files = []
    for file_path in base_path.rglob("*"):
        if (
            ".git" not in file_path.parts
            and file_path.is_file()
            and not is_binary(file_path)
        ):
            files.append(str(file_path))
    end_of_file_fixer.main(files)
