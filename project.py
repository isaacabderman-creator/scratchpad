from pathlib import Path
from modules.interface import console, list_dir_content, show_file_content
from modules.file import edit_file

MAIN_DIR: Path = Path("./college")


def main() -> None:
    console.print(show_file_content(MAIN_DIR, "example.md"))
    console.print(list_dir_content(MAIN_DIR))
    changes = edit_file(MAIN_DIR, "third.md")
    console.print(changes)


if __name__ == "__main__":
    main()
