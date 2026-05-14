from pathlib import Path
import texteditor


def edit_file(DIR: Path, file_name: str) -> str:
    path = Path(DIR) / file_name
    try:
        with path.open() as file:
            no_changes: int = len(file.readline())
    except FileNotFoundError:
        no_changes: int = 0
        with path.open("w") as file:
            file.write("Starting file\n")

    texteditor.open(filename=path)
    with path.open() as file:
        content = file.readline()
    return f"Lines added: {len(content) - no_changes}"
